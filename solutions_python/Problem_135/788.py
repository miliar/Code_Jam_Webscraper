import sys

T = int(sys.stdin.readline())
for case in range(0,T):
    ok = {x for x in range(1, 17)}
    for time in range(0,2):
        row = int(sys.stdin.readline()) - 1
        table = [{int(y) for y in sys.stdin.readline().split()} for x in range(0,4)]
        ok = ok & table[row]
    if len(ok) == 0:
        print("Case #%d: Volunteer cheated!" % (case+1))
    elif len(ok) == 1:
        print("Case #%d: %d" % (case+1, ok.pop()))
    else:
        print("Case #%d: Bad magician!" % (case+1))



    
