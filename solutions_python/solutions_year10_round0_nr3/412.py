from math import *

f = open('C-small-attempt0.in', 'r')
fout = open('Download C-small.out', 'w')
T=int(f.readline())
for i in xrange(0, T):
    string = f.readline()
    list = str.split(string,' ')
    R, k, N = (int(list[0]), int(list[1]), int(list[2]))
    print R, k, N
    
    grouplist=str.split(f.readline(),' ')
    for e in xrange(0, N):
        grouplist[e]=long(grouplist[e])
    print grouplist
        
    money =0
    ind=0
    for j in xrange(0, R):
        sum=0
        ind=0
        while True:
            sum+=grouplist[ind]
            if (sum<=k):
                money += grouplist[ind]
                ind+=1
                #print money
                if ind >= N:
                    break;
            else:
                break
        list=grouplist
        grouplist=list[ind:N]+list[0:ind]
        #print grouplist   
        value = 'Case #'+ str(i+1)+ ': '+ str(money)+'\n'
    fout.write(value)

f.close()
fout.close()
        
