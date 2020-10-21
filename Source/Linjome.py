#----- Imports Section -----
import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])

try:
    import pyautogui as pya
except:
    install('python3-xlib')
    install('scrot')
    install('python3-tk')
    install('python3-dev')
    install('pyautogui')
    import pyautogui as pya

try:
    import pyperclip
except:
    install('pyperclip')
    import pyperclip

try:
    from googletrans import Translator
except:
    install('googletrans')
    from googletrans import Translator

Nextline = '\r\n'
try:
    from pynotifier import Notification
except:
    install('py-notifier')
    from pynotifier import Notification

import re
import time

#----- Functions Section -----
def clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()

def trim(str):
    str=str.replace('[','')
    str=str.replace(']','')
    str=str.replace('None','')
    str = re.sub(r'\d+\.{0,1}\d+(e[-\+]){0,1}\d+','',str)
    str=str.replace(',,','')
    str=str.replace(', ,','')
    str=str.replace('\'','')
    return str

def translate(inp):
    translator = Translator()
    translated = translator.translate(inp, dest='fa')
    extra = translated.extra_data
    desc =inp+' ('+translated.src +')'+Nextline + translated.text + Nextline*2
    if extra['all-translations']:
        all_trans=extra['all-translations']
        for i in range(len(all_trans)):
            item= all_trans[i]
            desc += str(i+1)+'- '+item[0]+Nextline
            inner_item1 = item[1]
            desc += str(inner_item1).replace('[','').replace(']','')+Nextline
            for intem in item[2]:
                desc += intem[0] +' ('+str(intem[1]).replace('[','').replace(']','')+')'+Nextline
            desc+=Nextline
    desc = trim(desc)
    return desc

def notify(message):
    notif =Notification(
        title='ترجمک',
        icon_path='',
        description=message,
        duration=10,
        urgency=Notification.URGENCY_NORMAL
    ).send()

#----- Main Section -----
inp=clipboard()
text=translate(inp)
notify(text)




