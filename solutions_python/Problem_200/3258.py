T = input()

for i in range(int(T)):
    result = "Case #%d: " %(i+1)
    strList = list(input())
    N = [int(x) for x in strList]
    for j in range(len(N)-1, 0, -1):
        if N[j-1] > N[j]:
            N[j-1] = int(N[j-1]) - 1
            for k in range(j, len(N)):
                if N[k] == 9:
                    break
                N[k] = 9
                
    i = 0
    for d in N:
        if (d == 0):
            i += 1
            break
            
    for d in N[i:]:
        result += str(d)
    print(result)