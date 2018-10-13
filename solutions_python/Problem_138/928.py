import copy
import time
start_time = time.time()

def solve(Nm,Kn):
    Nm.sort(reverse=True)
    Kn.sort()
    cnt = 0
    for i in Nm:
        j =len(Kn)-1
        #print(len(Kn),j)
        while j>=0 and Kn[j]>i:
              j-=1
              #print(j)
        if j <0:
            #print(cnt,i,j)
            return cnt
        else:
            cnt+=1
            rm = Kn[j]
            Kn.remove(rm)
            #print(cnt,i,j,rm)
    return cnt
s=[0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.3, 0.992, 0.899]
t=[0.916, 0.728, 0.271, 0.52, 0.7, 0.521, 0.215, 0.341, 0.458]
#solve(s,t)    
def solve2(Nm,Kn):
    Kn.sort()
    Nm.sort()
    cnt = 0
    #print(Kn, Nm)
    for i in Nm:
        j = 0
        #print(i)
        if len(Kn)!=0:
            while(j<len(Kn) and Kn[j]<i):
                j+=1
                #print(j)
            if j==len(Kn):
                cnt+=1
                rm = min(Kn)
                Kn.remove(rm)
            else:
                rm = Kn[j]
                Kn.remove(rm)
            #print(rm,Kn)
        #print(cnt)
    return cnt
            

def run(file):
    a_in = open(file,encoding= 'utf-8')
    results = a_in.readlines()
    N = int(results[0].replace('\n',''))
    a_out = open('D_output.txt','w',encoding = 'utf-8')
    for i in range(1,N+1):
        tmp = 3*(i-1)+1
        #print(tmp)
        bs =float(results[tmp].replace('\n',''))
        Nm= list(map(float,results[tmp+1].replace('\n','').split()))
        Kn = list(map(float,results[tmp+2].replace('\n','').split()))
        tmp =copy.deepcopy(Nm)
        tmp1=copy.deepcopy(Kn)
        #print(bs,Nm,Kn)
        rels = "Case #"+str(i)+": "+str(solve(Nm,Kn))+" "+str(solve2(tmp,tmp1))
        a_out.write(rels+'\n')

run('D-large.in')
#run('D_t2.txt')
print (time.time() - start_time, "seconds")
#t=solve([30.50000,3.14159,1999.19990])
#t=solve([3,1,10000])
s=[0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.3, 0.992, 0.899]
t=[0.916, 0.728, 0.271, 0.52, 0.7, 0.521, 0.215, 0.341, 0.458]
#t=solve2(s,t)  

