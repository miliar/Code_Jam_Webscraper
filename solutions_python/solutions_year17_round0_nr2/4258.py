t = int(input())
count = 1

for case in range(t):
    n = input()
    i = n
    while(i != 0):
        nd = [int(d) for d in str(i)]
        l = len(nd)
        tidy = 1
        for j in range(l-1):
            if(nd[j] > nd[j+1]):
                tidy = 0
                break
        if(tidy):
            print("Case #"+str(count)+": "+str(int(''.join([ "%d"%x for x in nd]))))
            break
        i = i-1
    
    count = count + 1
    
    
