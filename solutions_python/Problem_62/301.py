def input() :
    t=int(raw_input())
    for i in xrange(0,t) :
        n=int(raw_input())
        lines=list()
        ans=0
        for j in xrange(0,n) :
            line=raw_input()
            line=line.split()
            lines.append(map(int,line))
        for j in xrange(0,n) :
            for k in xrange(0,j) :
                if(lines[j][0] < lines[k][0] and lines[j][1] > lines[k][1]) :
                    ans+=1
                elif(lines[j][0] > lines[k][0] and lines[j][1] < lines[k][1]) :
                    ans+=1
        print "Case #%d: %d" % (i+1,ans) 

if __name__ == "__main__" :
    input() 
