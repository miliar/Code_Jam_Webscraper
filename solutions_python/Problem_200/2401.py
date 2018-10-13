t = int(input())
for c in range(t):
    str_n = list(input()) 
    for _ in range(100):
        for idx in range(0, len(str_n)-1):
            if int(str_n[idx]) > int(str_n[idx+1]):
                str_n[idx] = str(int(str_n[idx])-1)
                for jdx in range(idx+1, len(str_n)):
                    str_n[jdx]='9'
                break
    print("Case #"+str(c+1)+": "+str(int(''.join(str_n))))



