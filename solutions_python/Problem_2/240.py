import sys

class traintime:
    def __init__(self, source, starthour, startmin, endhour, endmin):
        self.back = None
        self.next = None
        self.start = customtime(starthour, startmin)
        self.end = customtime(endhour, endmin)
        self.source = source
    def __str__(self):
        return "%s %s %s %s" %(str(self.back is not None), str(self.next is not None), self.start, self.end)

class customtime:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __cmp__(self, other):
        return cmp(self.hour*60+self.minute, other.hour*60+other.minute)

    def getAddMinutes(self, addmin):
        newmin = self.minute + addmin
        newhour = self.hour + newmin/60
        newmin = newmin%60
        return customtime(newhour, newmin)

    def __str__(self):
        return '%02d:%02d' % (self.hour, self.minute)



inputcases = int(sys.stdin.readline())
for case in range(inputcases):
    turnaround = int(sys.stdin.readline())

    (nA, nB) = [int(s) for s in sys.stdin.readline().split()]

    alltimes = []

    for i in range(nA):
        (starttimestr, endtimestr) = sys.stdin.readline().split()
        alltimes.append(traintime(0, int(starttimestr.split(':')[0]), int(starttimestr.split(':')[-1]), int(endtimestr.split(':')[0]), int(endtimestr.split(':')[-1])))

    for i in range(nB):
        (starttimestr, endtimestr) = sys.stdin.readline().split()
        alltimes.append(traintime(1, int(starttimestr.split(':')[0]), int(starttimestr.split(':')[-1]), int(endtimestr.split(':')[0]), int(endtimestr.split(':')[-1])))

    def startfirst(a, b):
        if a.start > b.start:
            return 1
        elif b.start > a.start:
            return -1
        else:
            return 0   
       
    alltimes.sort(startfirst)
    for starter in alltimes:
        if starter.next is None:
            current = starter
            while True:
                potential = [time for time in alltimes if time.source != current.source and time.back is None and current.end.getAddMinutes(turnaround) <= time.start]
                if len(potential) == 0:
                    break
                potential.sort(startfirst)
                chosen = potential[0]
                current.next = chosen
                chosen.back = current
                current = chosen

    if False:
        for time in alltimes:
            if time.back is None:
                print "Start", time.source,
                current = time
                while current is not None:
                    print current.start, current.end, '-',
                    current = current.next
                print
    
    print 'Case #%d: %d %d' %(case+1, len([time for time in alltimes if time.source == 0 and time.back is None]), len([time for time in alltimes if time.source == 1 and time.back is None]))
