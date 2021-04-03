import curses
from curses import wrapper
import socket
import threading

nickname = "rk"
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(('127.0.0.1',6969))

def logger():
    while True:
        try:
            content = connection.recv(1024).decode("ascii")
            if content == "NICK":
                connection.send(nickname)
            else:
                print(content)
        except:
            print("Error...")
            connection.close()
            break



def main(stdscr):
    stdscr.clear()

    curses.noecho()
    stdscr.keypad(True)
    height,width = stdscr.getmaxyx()

    x = 0

    def userInput(stdscr):
        msg = ""
        while True:
            char = stdscr.getkey()
            if char == "KEY_BACKSPACE":
                msg = msg[:-1]
            else:
                if ord(char) == 27:
                   return
                elif ord(char) in range(65,92) or ord(char) in range(97,123) or ord(char) == 32:
                   msg += char
                elif ord(char) == 10:
                   connection.send(msg.encode("ascii"))

            stdscr.refresh()
            stdscr.addstr(height-1,0,msg)

    userInputThread = threading.Thread(target=userInput,args=[stdscr])
    userInputThread.start()
    global logger
    threading.Thread(target=logger,).start()


wrapper(main)
