import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    curses.noecho()
    stdscr.keypad(True)
    height,width = stdscr.getmaxyx()

    x = 0

    while True:
        char = stdscr.getkey()
        if char == 'KEY_BACKSPACE':
            x -= 1
            continue
        elif ord(char) in range(65,92) or ord(char) in range(97,123):      
            stdscr.addch(height-1,x,char)
        x += 1

        #x += len(f"{ord(char)}")
        #stdscr.addstr(height-1,x,f"{ord(char)}")


wrapper(main)
