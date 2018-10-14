test = []
with open('B-small-attempt2.in') as f:
    for line in f :
        test.append(line[:-1])
f.close()
ind_ex = 0
while ind_ex < len(test) :
    t = int(test[ind_ex])
    ind_ex += 1
    for i in range(t) :
        num = int(test[ind_ex])
        ind_ex += 1
        if num < 10 :
            print "Case #{}: {}".format(i+1, num)
        else :
            while num > 0 :
                n = [int(l) for l in str(num)]
                ind = 0
                for k in range(len(n)-1) :
                    if n[k+1] >= n[k] :
                        ind = 1
                    else :
                        ind = 0
                        break
                if ind == 1 :
                    print "Case #{}: {}".format(i+1, num) 
                    break
                num -= 1
            
        