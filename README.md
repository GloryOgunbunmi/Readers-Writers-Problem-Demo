# Readers-Writers-Problem-Demo
this demonstrates the flaw in the Reader/Writers Problem

The Readers/Writers problem using Python's threading system: essential threading and Lock (mutex) elements 
In order to demostrate the flaw in the given algorithm, design follows:

1. the  demonstration must generate 100 threads with a 9:1 Reader/Writer ratio. So, for each writer you generate, your implementation must generate 9 readers. There must be a 2 second interval between creation of each thread. Please keep separate counts for readers and writers.
2. Each writer must remain in its critical region for a fixed 3 seconds, announcing its entry and exit around the critical region.
3. Readers read in the critical region for a random number of seconds between 3 and 5 second. Readers also must announce their entry and exit around the critical region.
4. After the last thread has been created, your demonstration must note the number of writers currently waiting to write and the current number of readers reading.

Note : the print statement in Python is not thread safe and can be preempted in the middle of a print. Becuse of this behavior, each print must use a Lock to ensure that each print can complete without interruption from another thread. Lock l1 is the lock used to protect print statements in the example below.
