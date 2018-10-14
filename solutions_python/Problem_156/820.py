#!/usr/bin/python
import sys

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
lines=lines[1:]
case=1

debug=False
#debug=True

def eatCakes(cakes):
    cakes = [ x - 1 for x in cakes]
    cakes = [ x for x in cakes if x > 0]

    return cakes


def doSpecial(cakes):

    if len(cakes) == 1:
        cake=cakes[0]
        newCake=cake / 2
        if cake == 9: 
            newCake = 3
        cake-=newCake
        cakes=[cake,newCake]
   
    else:
        cakes.sort()
        cakes.reverse()
        cake=cakes[0]
        cakes=cakes[1:]
        secCake=cakes[0]

        newCake= cake / 2
        if secCake < cake - 2 and secCake > 1:
            newCake = cake - secCake
#        if newCake > secCake:
#            newCake-=secCake/2
        cake-=newCake
        cakes.append(cake)
        cakes.append(newCake)

        
    cakes.sort()
    return cakes

def process(cakes):
    cakes = [ int(x) for x in cakes.split(' ')]
    cakes.sort()
    safety=max(cakes)
    minutes=0
    while len(cakes) > 0:
        if safety > minutes + max(cakes):
            safety = minutes+max(cakes)
        if debug:
            print("minutes: "+str(minutes)+"   cakes: "+str(cakes))

        if max(cakes) >= 3:
            cakes=doSpecial(cakes)
        else:
            cakes = eatCakes(cakes)
        minutes+=1

    if safety < minutes:
        minutes=safety
    
    return minutes


while len(lines) != 0:
    if lines[0] == '':
        break
    
    d=lines[0]
    cakes=lines[1]
    if debug:
        print("Case #"+str(case)+":")
    output=process(cakes)
    print("Case #"+str(case)+": "+str(output))
    case+=1
    lines=lines[2:]
	
	
