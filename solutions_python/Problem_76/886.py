def tobinary(dec_val, bin_list):
    cel = dec_val
    #bin_list=[]
    for d in xrange(19,-1,-1):
        bin_list.append(cel/(2**d))
        cel = cel%(2**d)

def Patrick_adding(bin_list1,bin_list2):
    for i in xrange(0,20):
        if bin_list1[i] != bin_list2[i]:
            bin_list1[i]=1
        else:
            bin_list1[i]=0

def equ(bin_list1, bin_list2):
    for i in xrange(0,20):
        if bin_list1[i]!=bin_list2[i]: return False
    return True

#main
T = input()
for i in xrange(0,T):
    N = input()
    s = raw_input()
    z = s.split(' ')
    bag = []
    maximum = 0
    for zz in z:
        bag.append(int(zz))
    #print bag
    s_s = 0
    for j in xrange(1,(2**N)/2):
        Patrick = []
        Sean = []
        n_binary = []
        Patrick_count = 0
        Sean_count = 0
        tobinary(j,n_binary)
        for k in xrange(0,N):
            if n_binary[19-k]==0:
                 Patrick.append(bag[k])
                 Patrick_count+=1
            else:
                 Sean.append(bag[k])
                 Sean_count+=1
        Patrick_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Sean_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        for k in xrange(0, Patrick_count):
            t=[]
            tobinary(Patrick[k],t)
            Patrick_adding(Patrick_sum,t)
        for k in xrange(0, Sean_count):
            t=[]
            tobinary(Sean[k],t)
            Patrick_adding(Sean_sum,t)
        if equ(Patrick_sum, Sean_sum):
            s_s+=1
            #print 'bazing'
            maximum_cand1 = 0L
            for k in xrange(0, Sean_count):
                maximum_cand1+=Sean[k]
            #print Sean, maximum_cand1
            maximum_cand2 = 0L
            for k in xrange(0, Patrick_count):
                maximum_cand2+=Patrick[k]
            #print Patrick, maximum_cand2
            if maximum_cand1>maximum_cand2:
                if maximum<maximum_cand1:
                    maximum=maximum_cand1
            else:
                if maximum<maximum_cand2:
                    maximum=maximum_cand2
            #print maximum_cand
    iii=i+1
    if s_s == 0:
        print 'Case #%i:'%iii, 'NO'
    else:
        print 'Case #%i:'%iii, maximum

