
import copy

T = int(raw_input())

for t in range(0,T):
    N = int(raw_input())
    nb = [float(x) for x in raw_input().split()]
    kb = [float(x) for x in raw_input().split()]

    nb.sort()
    kb.sort()

    dkb = copy.deepcopy(kb)

    #print nb
    #print kb

    # deceitful war
    dw_p = 0
    ln = len(nb)
    index = ln - 1;
    lost = 0;
    while(index >= lost):
        for i in range(len(dkb)-1, -1, -1):
            if nb[index] > dkb[i]:
                dkb.remove(dkb[i])
                break;
            else:
                lost = lost + 1
                dkb.remove(dkb[i])
        index = index - 1
    dw_p = ln - lost

    # optimal war
    ow_p = 0
    index = 0
    ln = len(nb)
    while(index < ln):
        state = False
        for i in range(0, len(kb)):
            if(nb[index] < kb[i]):
                kb.remove(kb[i])
                state = True
                break;
            else:
                continue
        if not state:
            kb.pop(0)
            ow_p = ow_p + 1
            
        index = index + 1

    print "Case #%d: %d %d" %(t+1, dw_p, ow_p)
