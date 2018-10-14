#!/usr/bin/python
import sys
def do_each_case():
    if debug: print "=================="
    Line = f.readline().rstrip("\n").split(' ')
    Smax = int(Line[0])
    Group = Line[1]
    
    #people in group

    min = 0;
    for num in range(1,Smax+1):
        pIng = 0;
        if int(Group[num]) == 0:
            Head = 0
        else:
            Head = num
        for x in range(0, num):
            pIng += int(Group[x])
        if  Head  <=  pIng:
            need = 0
        else:
            need = Head - pIng

        if debug:print "num: %d People in group: %s numInGroup:%s Head:%s need: %s min:%s" % (num,Group[0:num+1],pIng, Head,need, min)
        if need > min:
            min = need
        
    return min

filename=sys.argv[1]
if (len(sys.argv) == 3 and sys.argv[2] == "-d"):
    debug=True
else:
    debug=False
f=open(filename,'r')
CaseNum = int(f.readline().strip("\n"))
for c in range(1,CaseNum+1):
    ret = do_each_case()
    print "Case #%d: %s" % (c ,ret)


