

def getMin(c,f,x):
    time = 0.0
    v = 2
    t = 0.0
    ptime = x/2
    while True:
        t = c/v
        time = time + t
        #print 'v=%f, time=%f'%(v,t)
        v = v + f
        rtime = x/v+time
        #print 'rtime=',rtime
        if rtime>ptime:
            return ptime
        ptime = rtime
        
#print getMin(500,4.0,2000.0)

if __name__ == "__main__":
    input = open("B-large.in",'r');
    output = open("output.txt",'w');
    num = int(input.readline());
    i = 1;
    try:
        while i<=num:
            line = input.readline().split()
            c = float(line[0]);
            f = float(line[1]);
            x = float(line[2]);
            res = getMin(c,f,x);
            #print c,f,x
            #print "Case #%d: %.7f"%(i,res)
            output.write("Case #%d: %.7f"%(i,res));
            if i!=num:
                output.write('\n');
            i = i+1;
    finally:
        input.close();
        output.close();
    













