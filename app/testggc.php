<?php

require __DIR__.'/../vendor/autoload.php';

if(count($argv) === 2){
  $result = unserialize(base64_decode($argv[1]));
} else {
  print("php ".$argv[0]." <unserialize_payload_base64>");
}
