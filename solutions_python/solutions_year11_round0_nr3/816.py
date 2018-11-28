import sys


for _ in range(int(sys.stdin.readline())):
    nb=sys.stdin.readline()
    t=list(map(int, sys.stdin.readline().strip().split(" ")))
    a=t[0]
    b=t[0]
    for i in range(1,len(t)):
        a^=t[i]
        b+=t[i]
    if a==0:
        print("Case #"+str(_+1)+": "+str(b-min(t)))
    else:
        print("Case #"+str(_+1)+": "+"NO")

      
        
        
