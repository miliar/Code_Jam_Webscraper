def isOn(n, k):
    rest = k + 1
    pot = 2 ** n
    chunk = rest / pot
    rest -= chunk * pot
    while rest > 0:
        rest -= pot
    return not rest

class Switch:
    on = 0
    next = None

    def __init__(self, first, previous):
        self.first = first
        self.previous = previous

    def click(self):
        if self.on:
            if self.energy:
                if self.next:
                    self.next.click()
                self.on = False
        else:
             self.on = True

    @property
    def energy(self):
        if self.first:
            return True
        else:
            if self.previous.on and self.previous.energy:
                return True
            else:
                return False

def stupidIsOn(n, k):
    first = Switch(True, None)
    next = first
    previous = first
    last = first
    for i in range(n -1):
        last = Switch(False, previous)
        previous.next = last
        previous = last
    #import pdb;pdb.set_trace()
    for i in range(k):
        first.click()
    next = first
    while next:
        #print next.energy, next.on
        next = next.next
    return last.energy and last.on

count = int(raw_input())
i = 1
while i <= count:
    n, k = map(int, raw_input().split())
    if isOn(n, k):
        result = 'ON'
    else:
        result = 'OFF'
    print 'Case #%i: %s' % (i, result)
    i += 1
