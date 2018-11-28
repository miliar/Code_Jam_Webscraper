
T = int(input())
for t in range(T):
    s,k = input().split()
    s = list(s)
    #print("s: ", s)
    k = int(k)

    if '-' not in s:
        print("Case #" + str(t+1) + ": " + str(0))
        continue
    elif k == len(s) and '+' not in s:
        print("Case #" + str(t+1) + ": " + str(1))
        continue
    elif k == len(s):
        print("Case #" + str(t+1) + ": IMPOSSIBLE")
        continue

    d_from_end = len(s)
    num_flips = 0
    for i in range(len(s)):
        if d_from_end > k:
            if s[i] == '-':
                s[i] = '+'
                for j in range(1,k):
                    if s[i+j] == '-': s[i+j] = '+'
                    else: s[i+j] = '-'
                        
                num_flips += 1
                            
        else:
            end = s[len(s) - k:]
            #print("end: ", end)
            if '-' not in end:
                print("Case #" + str(t+1) + ": " + str(num_flips))
                break
            elif '+' not in end:
                print("Case #" + str(t+1) + ": " + str(num_flips + 1))
                break
            else: 
                print("Case #" + str(t+1) + ": IMPOSSIBLE")
                break

        d_from_end -= 1
        #print(s)
