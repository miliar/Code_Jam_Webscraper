fil = open('B-large.in','r')
arr= fil.readlines()
fil.close()

fil=open('test.out','w')
for case in range(1,int(arr[0])+1):
    line=arr[case].split(" ")
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    speed=2
    time=0
    while True:
        speed_new=speed+f
        time_new=time+c/speed+x/speed_new
        
        time_old=time+x/speed
        
        if (time_new < time_old):
            time=time+c/speed
            speed=speed_new
        else:
            time=time_old
            break
    answer='%.7f'%(time)
    fil.write("Case #"+str(case)+": "+answer+"\n")
fil.close() 


