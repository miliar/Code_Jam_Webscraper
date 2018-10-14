t = int(input())

for i in range(1, t + 1):
    n = input()
    
    while n >= 10:
        N = list(str(n))
        
        tidy = True
        
        for j in range(0, len(N) - 1):
            if int(N[j]) > int(N[j + 1]):
                N[j] = str((int(N[j]) - 1) % 10)
                N[j + 1:] = ['9'] * len(N[j + 1:])
                
                tidy = False
                
                break
        
        if tidy:
            break
        
        n = int(''.join(N))
    
    print("Case #{}: {}".format(i, n))