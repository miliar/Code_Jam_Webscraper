import sys
tempin = sys.stdin
tempout = sys.stdout
sys.stdout = open("A-small-output.txt", "w")
sys.stdin = open("A-Small-attempt0.in")
T=int(raw_input())
for x in range (1,(T+1)):
    _input=raw_input()
    List=_input.split(" ")
    Max=List[0]
    Levels=List[1]
    Levels=list(Levels)
    total=0
    req=0
    for i in range(int(Max)+1):
        
        
        if total >=i:
            total+=int(Levels[i])
            
        elif i>total:
            req+=1
            total+=int(Levels[i])
            total+=1
        
    print "Case #%d: %d" %(x,req)
sys.stdin.close()
sys.stdin = tempin
sys.stdout.close()
sys.stdout = tempout
        
    
    