def brute(pan , k):
    times = []
    lengthP = len(pan)-(k-1)
    #print('inizia il trip')
    for perm in perms(lengthP):
        #print('permutazione',perm)
        #print(pan)
        pan_test = pan[:]
        count = 0
        for i,b in enumerate(perm):
            if b == '1':
                pan_test= flip(pan_test, k, i)
                #print('flipped on', i, 'into',pan_test)
                count +=1
            #if b == '0':
        #print(count)
        if '-' not in pan_test:
            #print('risolto')
            times.append(count)
        #print()
    if times:
        return min(times)
    else:
        return 'IMPOSSIBLE'


def flip(pan,k,i):
    for l in range(k):
        target = i+l
        if pan[target] == '+':
            pan[target] = '-'
        else:
            pan[target] = '+'
    return pan


def perms(n):
    if not n:
        return
    for i in range(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s


'''
pan = list('---+-++-')
k= 3
i= 2

print('Result ------------',brute(pan,k))
'''

t = int(input())
for i in range(1, t + 1):
    pan, k = [s for s in input().split(" ")]
    pan=list(pan)
    k=int(k)
    print("Case #{}: {}".format(i,brute(pan,k)))