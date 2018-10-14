with open('/home/gauravjs/Documents/Google Code Jam/2014Q/inputfile2l','r') as f:
    cases=int(f.readline())
    lines=f.readlines()
inputs=[]
for i in range(cases):
    rate =2
    time =0
    cost,profit,win=lines[i].strip().split()
    cost=float(cost)
    profit=float(profit)
    win=float(win)
    mintime=win/rate
    time+=cost/rate
    rate+=profit
    while (time+(win/rate)<mintime):
        mintime=time+(win/rate)
        time+=cost/rate
        rate+=profit
    s=mintime

    print 'Case #'+str((i+1))+':',str(s)



#for y in range(len(inputs)):
#    i=inputs[y]
#    n,s,p=i[0],i[1],i[2]
#    x=0
#    for j in range(3,len(i)):
#        if i[j]>3*p-2:
#            x=x+1
#        elif i[j]>3*p-4 and s>0:
#            s=s-1
#            x=x+1
#    print 'Case #',y,': ',x
