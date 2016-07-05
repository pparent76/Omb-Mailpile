#!/bin/bash

mail=$(cat /home/www-data/mail);
gpg --fingerprint $mail 2>/dev/null| head -n 2 | tail -n 1 | sed 's/ //g' |cut -d'=' -f2-
