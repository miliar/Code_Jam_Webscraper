def play(a , mote, current):
    b=0
    if current < len(mote):

        if int(a) > int(mote[current]):
            a =int(a) + int(mote[current])
            current +=  1
            b = play(int(a) , mote, current)

        else:
            c=999999999999999
            if a != 1:
                c = play(int(a)+int(a)-1 , mote , current)
            d = play(a,mote,current +1)
            if c < d:
                b = c
                b+=1
    
            else:
                b = d
                b +=1

    return b
        
    
f = open("DATA1.txt")
g = open("OUT1.txt",'w')
n = f.readline().strip()
for x in range(int(n)):
    a, n = f.readline().strip().split(" ")
    mote = []
    for val in f.readline().strip().split():
        mote.append(int(val))
    current =0
    mote.sort()
    cont = True
    b = play(a, mote, current)
    print (b)
        
    
        
        
    g.write("Case #"+str(int(x+1))+": "+str(b)+"\n")
g.close()
