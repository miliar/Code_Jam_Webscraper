class Time(object) :
    def __init__(self, hours, minutes) :
        self.hours = hours
        self.minutes = minutes

    def __add__(self, offset) :
        t = Time(self.hours, self.minutes)
        t.minutes += offset
        if t.minutes >= 60 :
            t.hours += t.minutes // 60
            t.minutes %= 60

        return t

    def __lt__(self, other) :
        if self.hours != other.hours :
            return self.hours < other.hours

        return self.minutes < other.minutes

    def __str__(self) :
        return "(%02d:%02d)" % (self.hours, self.minutes)

    __repr__ = __str__

alist = [(Time(9, 0), Time(12, 0)),
             (Time(10, 35), Time(12, 30)),
             (Time(10, 0), Time(13, 0))]
blist = [(Time(9, 0), Time(10, 30)),
             (Time(12, 2), Time(15, 0))]

def counter(alist, blist, turnaround) :
    alist.sort()
    blist.sort()

    d = {0 : alist, 1 : blist}

    current = 0
    c = Time(0, 0)

    ac = 0
    bc = 0
    while alist or blist :
        if not d[0] :
            current = 1
        elif not d[1] :
            current = 0
        elif d[0][0] < d[1][0] :
            current = 0
        elif d[1][0] < d[0][0] :
            current = 1

        if current == 0 :
            ac += 1
        else :
            bc += 1

        next = d[current][0][1] + turnaround
        del d[current][0]

        while True :
            for index, i in enumerate(d[1 - current]) :
                if i[0] < next :
                    continue
                else :
                    del d[1 - current][index]
                    next = i[1] + turnaround
                    current = 1 -current
                    break
            else :
                break

    return "%s %s" % (ac, bc)

def main() :
    numTestCases = int(raw_input())
    for j in range(numTestCases) :
        turnaround = int(raw_input())
        a, b = (int(i) for i in raw_input().split())
        alist = []
        blist = []
        for i in range(a) :
            start, end = (raw_input().split())
            start = tuple((int(i) for i in start.split(':')))
            end = tuple((int(i) for i in end.split(':')))
            alist.append((Time(*start), Time(*end)))
        for i in range(b) :
            start, end = (raw_input().split())
            start = tuple((int(i) for i in start.split(':')))
            end = tuple((int(i) for i in end.split(':')))
            blist.append((Time(*start), Time(*end)))

        print "Case #%d: %s" % (j + 1, counter(alist, blist, turnaround))

main()





