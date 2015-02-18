from itertools import cycle
from threading import Timer

#prompts user to enter the beats per minute
x = int(raw_input("BPM:"))

#calculates the count interval using the user's BPM
metspeed = 60.0 / x 

#cycles through the defined range
counts = cycle(xrange(1, 5))

#prints the counts in the range in order one at a time
def visual():
    print next(counts)
    Timer(metspeed, visual).start()

#calls the visual function
visual()

