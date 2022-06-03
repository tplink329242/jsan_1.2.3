#!/bin/sh

#./jazzer --cp=json-sanitizer.jar --autofuzz=com.google.json.JsonSanitizer::sanitize

./jazzer --cp=json-sanitizer_Valid.jar --target_class="ValidJsonFuzzer" corpus
