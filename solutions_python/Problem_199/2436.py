def flip(line,start,count):
    j=0;
    i=start
    while(j<count):
        if(line[i]=='-'):
            line= line[:i] + '+' + line[(i+1):]
            i=i+1
        else:
            line= line[:i] + '-' + line[(i+1):]
            i=i+1

        j=j+1
    return line;

def flipcount(line,size):
    counter = 0;
    i=0
    temp = line
    while(i<len(line)):
        
        if(line[i]=='-'):
            rem = len(line)-i+1
           
            if(rem>size):
                line = flip(line,i,size);
            else:
                return "IMPOSSIBLE"
            #print line
            i=0
            counter=counter+1
            if(line==temp):
                return "IMPOSSIBLE"
        elif(line[i]=='+'):
            i=i+1
    return counter
t = int(raw_input())
l = []
z = []
x=0
while(x<t):
    p,q = raw_input().split()
    l.append(p)
    q=int(q)
    z.append(q)
    x=x+1
x=0
while(x<t):
    ans = str(flipcount(l[x],z[x]))
    print "case #%d: %s" % (x+1,ans)
    x=x+1



