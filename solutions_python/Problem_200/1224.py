
t = int(input())
for i in range(1, t+1):
    n = input()
    k = 0
    for j in range(len(n) - 1):
        if ord(n[j]) < ord(n[j+1]):
            k = j+1
        
        elif ord(n[j]) > ord(n[j+1]):
#            if k != 0 or :
            n = n[:k] + chr(ord(n[k]) - 1) + '9' * (len(n) - k - 1)
#            else:
#                n = '9' * (len(n) - 1)
            break
    
    
    if n[0] == '0':
        n = n[1:]
    print("Case #{}: {}".format(i, n))