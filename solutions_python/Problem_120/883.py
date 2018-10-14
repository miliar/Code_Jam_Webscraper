
file=open('A-small-attempt0.in','r')
wfile=open('output01','w')
number_of_cases= int(file.readline())





for x in xrange(number_of_cases):
    rings=0;
    count=1;
    
    second_line=str(file.readline())
    se_list=second_line.split()
    r=int(se_list[0])
    t=int(se_list[1])
    print str(r)+' '+str(t)
    while(1):
        paint_need=(r+count)*(r+count)-(r+count-1)*(r+count-1)
        t-=paint_need
        print paint_need
        if(t>=0):
            rings+=1
        else:
            wfile.write('Case #'+str(x+1)+': '+str(rings)+'\n')
            break
        count+=2
        
    



#wfile.write('Case #'+str(number_of_cases)+'\n')
