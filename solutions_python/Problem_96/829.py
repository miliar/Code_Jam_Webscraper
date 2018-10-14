def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        line = map(int,f.readline().split())
        n= line[0]
        p = line[1]
        goal = line[2]
        scores = line[3:]
        good = 0
        border = 0
        for j in scores:
            if j>=5:
                if j>= 3*goal -2:
                    good+=1
                elif j>=3*goal -4:
                    border+=1
            elif j==0:
                if goal==0:
                    good+=1
            elif j==1:
                if goal<=1:
                    good+=1
            elif j==2:
                if goal<=1:
                    good+=1
                elif goal==2:
                    border+=1
            elif j==3:
                if goal <=1:
                    good+=1
                elif goal==2:
                    border+=1
            elif j==4:
                if goal <=2:
                    good+=1
        g.write("Case #%d: " % (i+1))
        g.write("%d" % (good+min(border,p)))
        g.write("\n")
        continue
    f.close()
    g.close()
    
