t = int(input())
count = 1

for case in range(t):
    line = raw_input()
    s = line.split(' ')[0]
    k = int(line.split(' ')[1])

    slen = len(s)
    test = []
    test2 = []

    for i in range(slen):
        test.append('+')
        test2.append('-')
        
    if(s == "".join(test)):
        print("Case #"+str(count)+": 0")
    
    elif(s == ''.join(test2) and slen%k == 0):
        print("Case #"+str(count)+": "+str(slen/k))

    else:
        test2 = list(s)
        flip = 0
        for i in range(0,slen-k+1):
            if(test2[i] == '+'):
                continue
            
            else:
                flip = flip + 1
                test2[i] = '+'
                for j in range(i+1,i+k):
                    if(test2[j] == '-'):
                        test2[j] = '+'
                    else:
                        test2[j] = '-'
                
            if(''.join(test2) == ''.join(test)):
                print("Case #"+str(count)+": "+str(flip))
                break

        if(''.join(test2) != ''.join(test)):
            print("Case #"+str(count)+": IMPOSSIBLE")
    count = count + 1
    
    
