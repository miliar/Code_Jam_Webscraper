from operator import itemgetter, attrgetter, methodcaller
import math

def answer(N,K):
    if K == 1:
        minans = int(math.floor((N-1)*1.0/2))
        maxans = int(math.ceil((N-1)*1.0/2))
        ans = str(maxans)+" "+str(minans)
        return ans
    if N==K:
        return "0 0"
    if N%2 == 1:
        new_N= int(math.floor(N*1.0/2))
        new_K= int(math.ceil((K-1)*1.0/2))
        return answer(new_N, new_K)
    else:
        qualities=[]
        for i in xrange(N):
            qualities.append([i,i,N-1-i])
        ppleft=K
        while ppleft >0:
            qualities = sorted(qualities, key=itemgetter(0))
            qualities = sorted(qualities, key=lambda toilet: (min(toilet[1],toilet[2]),max(toilet[1],toilet[2])), reverse = True)
 #           print qualities
            loc_person=qualities[0][0]
  #          print "Removed:"+str(loc_person)
            for toilet in qualities:
                if toilet[0] < loc_person and loc_person-toilet[0] <=qualities[0][1]:
                    toilet[2]-=(qualities[0][2]+1)                    
                elif toilet[0] > loc_person and toilet[0]-loc_person <=qualities[0][2]:
                    toilet[1]-=(qualities[0][1]+1)
            if ppleft !=1:
                qualities=qualities[1:]
            ppleft-=1
        final_per=qualities[0]
        minans=min(final_per[1],final_per[2])
        maxans=max(final_per[1],final_per[2])
        ans = str(maxans)+" "+str(minans)
        return ans
            
            
T = input()

for i in xrange(T):
    case = raw_input()
    N, K = str(case).split()
    answera = answer(int(N),int(K))
    print "Case #"+str(i+1)+": "+answera


