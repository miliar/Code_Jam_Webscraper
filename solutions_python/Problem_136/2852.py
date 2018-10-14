__author__ = 'TM'
file = open('B-large.in','r')
out=open('B-large.out','w+')


samples=int(file.readline())
for x in range(samples):

    line=file.readline().strip()
    values=line.split()

    cost=float(values[0])
    FarmRate=float(values[1])
    Xwin=float(values[2])
    rate=2.0
    time=0.0
    while  (Xwin-cost)/rate > Xwin/(rate+FarmRate):
        time +=(cost/rate)
        rate +=FarmRate

    out.writelines ("Case #"+str(x+1)+": "+str("%.7f"%(time+Xwin/rate))+"\n")


