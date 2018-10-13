import math
data = open('C-small-2-attempt0.in','r')
d = open('C-small-2-attempt0.out','w')
tc = int(data.readline())
#tc = int(raw_input())
for t in range(tc):
#    tot, ppl = map(int,raw_input().split())
    tot, ppl = map(int,data.readline().split())
    lev = int(math.ceil(math.log(ppl+1,2)))-1
    max_up = int(tot//2**(lev))
    max_num = (tot%(2**lev)) +1
    if ppl > 2**lev-1 + max_num: max_up -= 1
    L_max = max_up /2;
    L_min = max_up - L_max - 1
#    print "Case #" + str(t+1) + ": " + str(L_max) + " " + str(L_min)
    print >>d, ("Case #" + str(t+1) + ": " + str(L_max) + " " + str(L_min))

d.close()
