import webbrowser
import time

counter = 3

print("This program started on "+time.ctime())
while counter > 0:
    webbrowser.open("https://www.youtube.com/watch?v=mrm50KbvGnk")
    time.sleep(10)
    counter = counter - 1


