'''
Created on May 8, 2010

@author: Paul
'''

class Snapper(object):
    def __init__(self, next=None):
        self.on = False
        self.power = False
        self.next = next
    def set_next(self, next):
        self.next = next
    def snap(self):
        if self.power and self.next:
            self.on = not(self.on)
    def powercheck(self):
        if self.power and self.next and self.on:
            self.next.power = True
        elif not(self.next):
            pass
        else:
            self.next.power = False

def convert(state):
    if state:
        return 'ON'
    else:
        return 'OFF'

def solve(n, k, casenum):
    # n = 4
    # k = 47
    on = False
    snappers = []
    previous = Snapper()
    for count in xrange(n):
        temp = Snapper()
        previous.next = temp
        previous = temp
        snappers.append(temp)
    light = Snapper()
    snappers[0].power = True
    snappers.reverse()
    snappers[0].next = light
    for count in xrange(k):
        for snapper in snappers:
            snapper.snap()
        snappers.reverse()
        for snapper in snappers:
            snapper.powercheck()
        snappers.reverse()
    on = light.power
    return 'Case #' + str(casenum) + ': ' + convert(on)    

def main():
    file = open('A-small.in')
    num_input = 0
    case_num = 1
    # output = open('output.txt', 'w+')
    for line in file:
        if not(num_input):
            num_input = line.split()[0]
        else:
            inp = line.split()
            n = int(inp[0])
            k = int(inp[1])
            # output.write(solve(n, k, case_num) + '\n') 
            print solve(n, k, case_num)
            case_num += 1
    # for snapper in snappers:
    #    print snapper

if __name__ == '__main__':
    main()