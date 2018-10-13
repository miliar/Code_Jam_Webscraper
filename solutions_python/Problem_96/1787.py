f = open('../data/2.txt','rb')
out = open('../data/2.out','wb')

d = {}


C = int(f.readline())

for i in range(1, C+1):
    line = [int(k) for k in f.readline().strip().split()]
    N = line[0]
    S = line[1]
    P = line[2]
    t = line[3:]
    #already larger
    cnt1 = 0
    #could be larger
    cnt2 = 0
    for n in t:
        if n % 3 == 0:
            if n / 3 >= P:
                cnt1 += 1
            if n / 3 == P - 1 and n / 3 >= 1:
                cnt2 += 1
        elif n % 3 == 1:
            if n / 3 + 1 >= P:
                cnt1 += 1
        else:
            if n / 3 + 1 >= P:
                cnt1 += 1
            if n / 3 + 1 == P - 1 and n / 3 >= 1:
                cnt2 += 1
    cnt1 += min(cnt2, S)
            
    out.write("Case #" + str(i) + ": " + str(cnt1)+"\n")    
    
