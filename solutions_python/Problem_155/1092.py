#!/usr/bin/python
import sys

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
lines=lines[1:]
case=1



def processCase(mx, vals):
    if len(vals) == 1:
        return 0
    invites=0
    cNeed=int(mx)
    c=int(vals[0])
    vals=vals[1:]
    thresh=1
    while len(vals) > 0:
        person=int(vals[0])
        if person == 0:
            vals=vals[1:]
            thresh+=1
        else:
            if c >= thresh:
                c+=person
                vals=vals[1:]
                thresh+=1
            else:
                invites+=1
                c+=1
    
#    print("c: "+str(c))
#    print("cNeed: "+str(cNeed))
#    print("")
    return invites
    


for line in lines:
    if line == '':
        break
    [mx,vals]=line.split(' ')
    output=processCase(mx,vals)
    print("Case #"+str(case)+": "+str(output))
    case+=1
	
	
