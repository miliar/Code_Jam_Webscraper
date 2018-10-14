#!/usr/bin/python

import sys



class Wait():
    """Read a queue from the string and manage the next group pointer"""
    def __init__(self, txt):
        self.groups = [ int(x) for x in txt.split() ]
        self.N = len(self.groups)
        self.start = None
        self.last = self.N-1
        
    def __iter__(self):
        """Start an iterator, at max it can be all the group at the same time"""
        self.start = self.last
        self.stop = False
        return self

    def next(self):

        if self.stop:
            raise StopIteration
        
        # Calculate the next one
        nxt = (self.last+1) % self.N
        if nxt==self.start:
            self.stop = True
        self.last = nxt
        return self.groups[nxt]

def Roller(roll, waitlist):
    (R,k,N) = [ int(x) for x in roll.split() ]
    W = Wait(waitlist)

    # Initially nobody has been refused
    last_group = 0
    Money = 0
    for i in xrange(R):
        # Fill the roller
        persons = last_group
        last_group = 0
        for group in W:
            if (persons+group)>k:
                # Refuse this last group
                last_group = group
                break
            else:
                persons += group
        # Ready to roll!!!
        Money += persons 
    return Money


def main(nameIn, nameOut):
    """Read form the input and write thr Case #:"""

    
    fI = open(nameIn, 'r')
    fO = open(nameOut, 'w')

    # First line is the number of cases
    l = fI.readline()
    Nl = int(l[0:-1])

    i=0
    roller = None
    waitlist = None
    for line in fI:
        line = line.strip() # This will remove the \n also
        if len(line)==0:
            continue

        if roller is None:
            roller = line
            continue
        waitlist = line
        # Now we can create a case
        i += 1
        if i>Nl:
            break
        Money = Roller(roller, waitlist)
        roller = None
        fO.write("Case #" + str(i) + ": " + str(Money) + "\n")
    fI.close()
    fO.close()


if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: " + sys.argv[0] + " <file_in> <file_out>")
        exit(0)

    main(sys.argv[1], sys.argv[2])



