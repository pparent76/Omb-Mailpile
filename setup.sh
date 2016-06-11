#!/bin/bash

unset HISTFILE
killall python2
echo $1>/tmp/mail
echo $2>/tmp/pass
echo $3>/tmp/fn

echo "Mail!!!!!!!!!!!!!!!!!!!"
cat /tmp/mail

sleep 2
rm -r ~/.local/share/Mailpile/
./mp --www=127.0.0.1:33411/Mailpile/
./mp --setup
sleep 1;
cat setup-commands | ./mp 
sleep 10
python2.7 setup-account.py
cp last-commands last-commands.tmp
sed -i "s/MAIL/$1/g" last-commands.tmp
#user=$(echo $1 | cut -f1 -d"@")
#sed -i "s/mailpile/$user/g" last-commands.tmp
cat last-commands.tmp | ./mp 
./mp --www=127.0.0.1:33411/Mailpile/ --wait > /dev/null 2>&1 </dev/null &
rm /tmp/pass
rm /tmp/mail
rm /tmp/fn
history -c
echo "finend"
exec >&-
exec 2>&-

