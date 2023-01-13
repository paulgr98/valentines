import PySimpleGUI as sg
import tomllib as tml
import json
import sys

icon = './heart.ico'

try:
    with open('config.toml', 'rb') as f:
        config = tml.load(f)
except FileNotFoundError:
    sg.popup('File "config.toml" not found...', title='Opps!', button_type=sg.POPUP_BUTTONS_OK)
    sys.exit()

lang = config['app']['lang']

try:
    with open('msg.json', 'r', encoding='utf-8') as f:
        msg = json.load(f)
except FileNotFoundError:
    sg.popup('File "msg.json" not found...', title='Opps!', button_type=sg.POPUP_BUTTONS_OK)
    sys.exit()

# check if the language is supported in msg.json
if lang not in msg:
    lang = 'en'

sg.popup(msg[lang]['msg1'], title='xD', button_type=sg.POPUP_BUTTONS_OK, icon=icon)

sg.popup(msg[lang]['msg2'], title='Hmmm', button_type=sg.POPUP_BUTTONS_OK, icon=icon)

choice, _ = sg.Window(
    '❤',
    [[sg.T(msg[lang]['msg3'])],
     [sg.Yes(s=10, button_text=msg[lang]['yes']), sg.No(s=10, button_text=msg[lang]['no'])]],
    icon=icon,
    disable_close=True).read(close=True)


def thanks() -> None:
    global icon
    sg.popup(msg[lang]['msg4'], title='❤', button_type=sg.POPUP_BUTTONS_OK, icon=icon)


if choice == msg[lang]['no']:
    for i in range(5):
        choice, _ = sg.Window(
            '❤',
            [[sg.T(msg[lang]['msg5'])],
             [sg.Yes(s=10, button_text=msg[lang]['yes']), sg.No(s=10, button_text=msg[lang]['no'])]],
            icon=icon,
            disable_close=True).read(close=True)
        if choice == msg[lang]['yes']:
            thanks()
            break
    else:
        sg.popup(msg[lang]['msg6'], title='...', button_type=sg.POPUP_BUTTONS_OK, icon=icon)
else:
    thanks()
