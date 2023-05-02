#Aduragbemi Ogunbunmi
#Operating Sysytems- CSCI
#Readers/Writers Demo
#Jeff Byron

from time import sleep
from threading import Thread
from threading import Lock
import random

#creates Locks
readers_lock = Lock()
writers_lock = Lock()
l1 = Lock()

#create counter
readers = 0
writers = 0
 
def writer(tnum):
    global writers #allow access to variable
    #aquire lock protecting counter
    with writers_lock:
        #update the counter
        writers += 1
    with l1:
        print('Writer {} has entered'.format(tnum))
    #block
    sleep(3)
    with l1:
        print('Writer {} has exit'.format(tnum))
    with writers_lock:
        #update counter
        writers -= 1
 
def reader(tnum):
    global readers
    #aquire lock protecting counter
    with readers_lock:
        #update counter
        readers += 1 
        if readers == 1:
            #acquire writer lock
            writers_lock.acquire()
    with l1:
        print('Reader {} has entered'.format(tnum))
    sleep(random.uniform(3,5))
    with l1:
        print('Reader {} has exit'.format(tnum))
    with readers_lock:
        #update counter
        readers -= 1
        if readers == 0:
            #release lock
            writers_lock.release() 
#create 100 thread 9:1 reader/writer thread
for i in range(100):
    if i % 10 == 0: 
        # create and configure a new thread
        thread = Thread(target=writer, args=(i,))
    else:
        #create threads
        thread = Thread(target=reader, args=(i,))
    #start  thread
    thread.start()
   #wait between each thread creation
    sleep(2)
 
with l1:
    print('Readers reading:', readers)
    print('Writers waiting:', writers)
    thread.join()

