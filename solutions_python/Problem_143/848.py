cases = int(raw_input())

for case_index in range(1,cases+1):
    input = raw_input().split()
    A,B,K = int(input[0]),int(input[1]),int(input[2])
    count = 0
    for i in range(A):
        for j in range(B):
            r = i&j
            if r<K:
                #print i,j
                count+=1
    print "Case #%d: %d"%(case_index,count)
