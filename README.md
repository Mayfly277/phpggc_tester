# PHPGGC tester

- quick & dirty POC project to test phpggc payload
- versions and checkout are based on composer
- modify phpggc_tester.py to configure phpggc and composer.phar path, change package to test and rce payloads
- only function call with __destruct vector is supported by now

## results 
- monolog/monolog results :
[![asciicast](https://user-images.githubusercontent.com/23179648/117204517-aeb84400-adf0-11eb-9f6f-9f707116ee2e.png)](https://asciinema.org/a/stF11x8m49tPiRSKqyoXaPase)

- laravel/laravel results  (with monolog as it is a requirement of laravel/framework)

![laravel](./img/laravel_6.0.0-8.x.png)

![laravel](./img/laravel_5.0.0-5.x.png)

![laravel](./img/laravel_4.0.0-4.x.png)

- symfony/symfony results : (- means composer error, not tested)

![symfony](./img/symfony5.x.png)

![symfony](./img/symfony4.2-4.x.png)

![symfony](./img/symfony4.x-4.1.x.png)

low versions are all KO :(