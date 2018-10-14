import sys



def flip(pan,size,index):
    if(len(pan)<size+index):
        return pan
    else:
        for i in range(index,index+size):
            if(pan[i]==1):
                pan[i]=0
            elif(pan[i]==0):
                pan[i] = 1
            else:
                raise Exception("WTF")
        return pan


def toarray(pan_String):
    pan=[]
    for i in pan_String:
        if (i == '+'):
            pan.append(1)
        elif (i == '-'):
            pan.append(0)
        else:
            raise Exception("WTF")
    return pan

def check(pan):
    for i in pan:
        if(i!=1):
            return False
    return True

out=open("out.txt","w")
with open("input.txt","r") as f:
    n=int(f.readline().strip())
    for k in range(n):
        s=f.readline().strip()
        size=int(s.split()[1])
        pan_s=s.split()[0]
        pan=toarray(pan_s)
        #print (pan)


        steps=0
        if ( not check(pan)):
            for i in range (len(pan)):
                for i in range (len(pan)):
                    if(pan[i]==0):
                        pan=flip(pan,size,i)
                        #print (pan)
                        steps+=1
                if(check(pan)):
                    break
        if (check(pan)):
            print "Case #%d: %d" % (k+1,steps)
            out.write("Case #%d: %d\n" % (k+1,steps))
        else:
            out.write("Case #%d: IMPOSSIBLE\n" % (k + 1))
