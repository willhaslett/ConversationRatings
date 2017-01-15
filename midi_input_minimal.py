import time
from pyo import *
pm_list_devices()

s = Server()
s.setMidiInputDevice(0)
s.boot()
s.start()

m = Midictl(ctlnumber=[2], minscale=0, maxscale=100)

while True:
    time.sleep(.1)
    print m.get(True)