import time
import webbrowser

total_breaks = 3
break_count = 0


print("This break started on" + time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=I_izvAbhExY")
    break_count = break_count + 1
    
