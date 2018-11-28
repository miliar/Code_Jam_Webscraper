import string

def Saving_Universe(selist,qlist):
    sw=0
    dflag=0
    while len(qlist)>0:
        bestid=0
        beststep=0
        index=0
        for se in selist:
            try:
                temp=qlist.index(se)
            except ValueError:
                dflag=1
                break
            if temp>beststep:
                beststep=temp
                bestid=index
            index +=1
        
        if dflag==1 :
            break
        #print qlist[beststep]
        qlist=qlist[beststep:]
        #print qlist
        sw +=1
    return sw
        

    
pid=1
ff=open("A-large.in")
ww=open("A-large.out","w")
ll=ff.readline()
num=string.atoi(ll)
while pid<=num:
    #print "++++++++++++++%d++++++++++++++++++++++"%(pid)
    ll=ff.readline()
    se_num=string.atoi(ll)
    se_list=[]
    for i in range(se_num):
        ll=ff.readline()
        se_list.append(ll)
    ll=ff.readline()
    q_num=string.atoi(ll)
    q_list=[]
    for i in range(q_num):
        ll=ff.readline()
        q_list.append(ll)

    dd=Saving_Universe(se_list,q_list)
    ww.write("Case #%d: %d\n"%(pid,dd))
    
    pid +=1    
ff.close()
ww.close()
