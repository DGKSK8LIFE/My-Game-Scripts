import keyboard

def autohop():
    while keyboard.is_pressed('space'):
        keyboard.send('space')

autohop()
