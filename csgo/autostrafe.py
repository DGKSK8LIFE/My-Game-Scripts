import keyboard

def autostrafe(left_strafe_key, right_strafe_key, interval):
    while True:
        keyboard.send(left_strafe_key, delay=interval)
        keyboard.send(right_strafe_key, delay=interval)

autostrafe('a', 'd', 0.5)
