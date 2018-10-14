import sys


n = int(raw_input())
#n = int(sys.stdin.readline())

for j in range(n):
    a = raw_input()
    #a = sys.stdin.readline()
    smax ,people = a.split()
    s_max = int(smax)
    people = map(int,people)

    sum = people[0]
    cum_sum = 0
    count = 0

    for i in range(1,len(people)):
        cum_sum = cum_sum + people[i-1]
        if i > cum_sum:
            count +=1
            cum_sum += 1

    print("Case #{0}: {1}".format(j+1,count))
    
    
            
            
        

    
