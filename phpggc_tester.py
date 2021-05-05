#!/usr/bin/env python3
import subprocess
import re
from rich import print
import os
from rich.progress import Progress
from rich.table import Table

# args
package = "monolog/monolog"
# package="laravel/laravel"
# package="guzzlehttp/guzzle"

phpggc = ['Monolog/RCE1', 'Monolog/RCE2', 'Monolog/RCE3', 'Monolog/RCE5', 'Monolog/RCE6']

#  config
composer_bin = "composer.phar"
phpggc_bin = "../phpggc/phpggc"
needle_string = 'ok123456789ok'


def delete_file(file):
    if os.path.exists(file):
        os.remove(file)


print("[blue] Start %s test[/blue]" % package)
delete_file('composer.json')
delete_file('composer.lock')
result = subprocess.run(['composer', 'show', '-a', package], stdout=subprocess.PIPE)
text = result.stdout.decode('utf-8')
versions = re.search(r'versions :(.*)\ntype', text).group(1)
print(versions)
results = {}

table = Table("PHP GGC %s" % package)
table.add_column('Package version', justify='right', style="bright_yellow")
for payload in phpggc:
    table.add_column(payload, justify='center')

versions_list = [x.strip() for x in versions.split(',')]
with Progress() as progress:
    task1 = progress.add_task("[cyan]checking versions...", total=len(versions_list))
    for version in versions_list:
        subprocess.run(['php', composer_bin, 'require', '-q', '%s:%s' % (package, version)])
        results = []
        find = '[red]KO[/red]'
        for phpggc_payload in phpggc:
            payload = subprocess.run([phpggc_bin, '-b', phpggc_payload, 'system', 'echo ' + needle_string],
                                     stdout=subprocess.PIPE).stdout.decode('utf-8')
            result = subprocess.run(['php', 'app/testggc.php', payload], stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout.decode('utf-8')
            if needle_string in result:
                results.append('[green]OK[/green]')
                find = '[green]OK[/green]'
            else:
                results.append('[red]KO[/red]')
        progress.update(task1, advance=1, description='[cyan]Checking versions... [/cyan] %15s' % version)
        table.add_row(find, version, *results)

print('[blue] === Results === [/blue]')
print(table)
