import datetime #a libary for displaying current time in HH:MM:SS
import time
import os

print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Starting server...")
time.sleep(4)
print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Creating world...")
time.sleep(8)
print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Creating world... Done")
time.sleep(0.3)
print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Server ready for players. Port: 12312")
print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] For list of avalible commands type help.")
while True:
    cmd = str(input())
    if cmd == "about":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Minecraft server emulator made by Alexey Denisov in Russia, Tula")
    elif cmd == "stop":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Stopping server...")
        time.sleep(4)
        os.system("pause")
        quit()
    elif cmd == "say":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Say what?")
        saytext = str(input())
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] [Server]> {saytext}")
    elif cmd == "help":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Avalible commands: about, stop, say, help")
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Syntax for command help: help <command> or help")
    elif cmd == "help about":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] about: About this server core")
    elif cmd == "help stop":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] stop: Stops the server")
    elif cmd == "help say":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] say: Print message to Minecraft chat")
    elif cmd == "help help":
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] help: Displays command list")
    else:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Unknown command. Type help for avalible commands list.")
