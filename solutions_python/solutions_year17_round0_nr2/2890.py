


t = int(input())  # read a line with a single integer
for b in range(1, t + 1):
    
    n = list(input())
    eqInd = 0
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            n[eqInd] = str(int(n[eqInd]) - 1)
            n[eqInd + 1:] = ['9'] * (len(n) - eqInd - 1)
            break
        
        if n[i] == n[eqInd]:
            continue
        elif n[i] == n[i-1]:
            eqInd = i - 1
            continue
        else:
            eqInd = i
            
    if n[0] == '0': n = n[1:]
                   
    print("Case #{}: {}".format(b, ''.join(n)))
