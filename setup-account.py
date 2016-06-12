import os
import random
import time

from mailpile.config.manager import ConfigManager
import mailpile.config.manager
import mailpile.config.defaults
import mailpile.security as security
from mailpile.crypto.gpgi import GnuPGKeyGenerator
from mailpile.plugins import PluginManager
from mailpile.plugins.contacts import AddProfile, ListProfiles, AddVCard, VCardCommand, ProfileVCard
from mailpile.commands import Command, Action
from mailpile.eventlog import Event
from mailpile.i18n import gettext as _
from mailpile.i18n import ngettext as _n
from mailpile.mailutils import Email, ExtractEmails, ExtractEmailAndName
from mailpile.mailutils import AddressHeaderParser
from mailpile.security import SecurePassphraseStorage
from mailpile.vcard import VCardLine, VCardStore, MailpileVCard, AddressInfo
from mailpile.util import *
from mailpile.ui import ANSIColors, Session, UserInteraction, Completer
import mailpile.util
import mailpile.config.defaults
from mailpile.commands import COMMANDS, Command, Action
from mailpile.config.manager import ConfigManager
from mailpile.conn_brokers import DisableUnbrokeredConnections
from mailpile.i18n import gettext as _
from mailpile.i18n import ngettext as _n
from mailpile.plugins import PluginManager
from mailpile.plugins.core import Help, HelpSplash, Load, Rescan, Quit
from mailpile.plugins.motd import MessageOfTheDay
from mailpile.ui import ANSIColors, Session, UserInteraction, Completer
from mailpile.util import *

_plugins = PluginManager(builtin=__file__)

# This makes sure mailbox "plugins" get loaded... has to go somewhere?
from mailpile.mailboxes import *




mailpile.i18n.ActivateTranslation(None, ConfigManager, None)
config = ConfigManager(rules=mailpile.config.defaults.CONFIG_RULES)
cfg=config
with open('/tmp/pass', 'rb') as fort1f3:p1=fort1f3.read()
pass2 = SecurePassphraseStorage(p1)
cfg.load_master_key(pass2)

session = Session(config)
cli_ui = session.ui = UserInteraction(config)
session.main = True
config.clean_tempfile_dir()
config.load(session)
session.config=cfg

vcard = MailpileVCard()
vcard.kind='profile'
with open('/tmp/mail', 'rb') as fort3f3:mail=fort3f3.read()
with open('/tmp/fn', 'rb') as fort2f3:fn=fort2f3.read()
mail.replace("\n", "")
fn.replace("\n","")
mail=''.join(mail.splitlines())
fn=''.join(fn.splitlines())
data= {'name': [fn], 'email': [mail],'route-protocol':['smtp'],'route-host':['::1'],'route-port':['25'],'route-auth_type':['none']}

command=Command(session,data=data)
command.session=session
addvcard=AddVCard(VCardCommand(command))
addvcard.session=session
profile=AddProfile(addvcard)
profile.session=session;
profile.data=data
vcard.config=cfg
print "before update"
print mail
print fn
profile._update_vcard_from_post(vcard)
print "after update"

#profile._create_new_key(vcard, "RSA4096",session)


#vcard.save();
print "before save vcards"
cfg.vcards.add_vcards(vcard)
print "after save vcards"
cfg.save()
print "after cfg save"
print "end file"
