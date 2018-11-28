T = int(input())

for t in range(1, T+1):
    N = input()

    inv = len(N)
    same = 0

    i = 0
    while i < len(N) - 1:
        i += 1
        if N[i-1] > N[i]:
            inv = i
            break

    if inv == len(N):
        num = N
    else:
        i -= 1
        c = N[i]
        while i >= 0 and N[i] == c:
            i -= 1
            same += 1

        num = ''
        num += N[:inv - same]
        num += str(int(N[inv - same]) - 1)
        num += '9' * (len(N) - inv + same - 1)
        num = int(num)


    #print(N)
    #print(' '*inv + '|' + ' '*(len(N) - inv))
    #print(' '*(inv - same) + '|')


    print('Case #{}: {}'.format(t, num))