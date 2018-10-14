def manager(n,k):
    lista=[n]
    #print('lista iniziale', lista)
    while k>0:
        k-=1
        maxi = max(lista)
        max_index = lista.index(max(lista))
        #print('max', maxi, max_index)
        if maxi % 2 == 0:
            right = (maxi // 2)
            left = right-1
        elif maxi % 2 == 1:
            left = (maxi-1)//2
            right = left
        lista = lista[:max_index] + [left, right] + lista[max_index + 1:]
    y = max(left, right)
    z = min(left, right)
    return [y,z]



def manager2(n,k):
    #print(' - NEW function testing = ',n,',',k)
    binary = bin(k)[2:]
    binary = binary[::-1]
    #print( k, 'in binary is', binary)
    for path in binary:
        #print ('number',n)
        if n % 2 == 0:
            right = (n // 2)
            left = right-1
        elif n % 2 == 1:
            left = (n-1)//2
            right = left
        #print('left', left,'right', right)

        if path == '1':
            n= left
            #print('go left 1')
        if path == '0':
            n = right
            #print('go right 0')

    y = max(left, right)
    z = min(left, right)
    return [y, z]

#n= 10**18
#k= 10**18
#print(' TESTING = ', n, ',', k)
#print(' - OLD result',manager(n,k))
#print(' - NEW result ',manager2(n,k))



t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    result = manager2(n,k)
    print("Case #{}: {} {}".format(i, result[0], result[1]))
