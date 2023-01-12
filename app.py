import PySimpleGUI as sg

icon = './heart.ico'

sg.popup('Twój komp został zhackowany xD LOL', title='xD', button_type=sg.POPUP_BUTTONS_OK, icon=icon)

sg.popup('Jednakże mam jedno pytanie...', title='Hmmm', button_type=sg.POPUP_BUTTONS_OK, icon=icon)

choice, _ = sg.Window(
    '❤️',
    [[sg.T('Będziesz moją walentynką?')],
     [sg.Yes(s=10, button_text='Tak'), sg.No(s=10, button_text='Nie')]],
    icon=icon,
    disable_close=True).read(close=True)


def thanks():
    global icon
    sg.popup('Yaaay, dziękuję ♥♥♥♥♥', title='❤️', button_type=sg.POPUP_BUTTONS_OK, icon=icon)


if choice == 'Nie':
    for i in range(5):
        choice, _ = sg.Window(
            '❤️',
            [[sg.T('Proszę :c')],
             [sg.Yes(s=10, button_text='Tak'), sg.No(s=10, button_text='Nie')]],
            icon=icon,
            disable_close=True).read(close=True)
        if choice == 'Tak':
            thanks()
            break
    else:
        sg.popup('Pierdol się...', title='...', button_type=sg.POPUP_BUTTONS_OK, icon=icon)
else:
    thanks()
