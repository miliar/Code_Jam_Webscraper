'''
Created on 12-Apr-2014

@author: savs95
'''


fp=open("war.in","r")
fo=open("output.txt","w")
cases=int(fp.readline())
for i in range(cases):
    no=int(fp.readline())
    naomi=fp.readline().split()
    ken=fp.readline().split()
    for k in range(no):
        naomi[k]=float(naomi[k])
        ken[k]=float(ken[k])
    naomi.sort() , ken.sort()
    '''print naomi, ken
    smaller=0
    larger=0
    for k in range(no):
        if(ken[0]>naomi[k]):
            smaller+=1
        else:
            break
    for k in range(no):
        if(ken[no]>naomi[no-1-k]):
            larger+=1'''
    #print naomi, ken
    point =0       
    naomi_w=naomi[:]
    ken_w = ken[:] 
    while(len(ken)!=0):
        if ken[-1]<naomi[-1]:
            x = ken.pop(0)
            for f in naomi:
                if f - x > 0:
                    naomi.pop(naomi.index(f))
                    point+=1
                    break
                
        else:
            x=ken.pop()
            naomi.pop(0)
    #print point        
    point_w=0
    while(len(ken_w)!=0):
        if naomi_w[-1]>ken_w[-1]:
            naomi_w.pop()
            ken_w.pop(0)
            point_w+=1
        else:
            x=naomi_w.pop()
            for f in ken_w:
                if f - x > 0:
                    ken_w.pop(ken_w.index(f))
                    break
    #print "Case #",i+1,": ", point," ", point_w
    string="Case #"+str(i+1)+": "+str(point)+" "+str(point_w)+"\n"
    fo.write(string)
fp.close()
fo.close()    