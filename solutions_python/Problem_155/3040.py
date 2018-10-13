import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)
rl = lambda: sys.stdin.readline().strip()

def compute():
    """ Code implementation """
    inline = rl()
    [shyness, audiences] = inline.split()
    shyness = int(shyness)
    cumsum = 0
    invite = 0
    audiences = audiences.strip()
    for k in range(shyness+1):
        if k > cumsum:
            invite = invite + (k-cumsum)
            cumsum = (k-cumsum) + cumsum
        cumsum = cumsum + int(audiences[k])
    return invite
if __name__ == '__main__':
    for i in range(int(rl())):  # The first line is usually # of cases
        print "Case #%d: %s" % (i+1, compute())