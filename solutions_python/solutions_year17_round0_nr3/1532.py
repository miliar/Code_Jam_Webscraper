import sys
import math
for C in range(1, int(sys.stdin.readline())+1):
    answer = 0
    N, K = [int(_) for _ in sys.stdin.readline().split()]
    slots = []
    new_slots = [N]
    for i in range(1, K+1):
        if not slots or slots[0] == 0:
            slots = sorted(new_slots)
            new_slots = []
        slot = slots.pop()-1
        if slot == 0:
            answer = [0, 0]
            break
        new_slots.extend([slot/2+slot%2, slot/2])
        answer = new_slots[-2:]
    print "Case #%s: %s" % (C, " ".join(map(str, answer)))