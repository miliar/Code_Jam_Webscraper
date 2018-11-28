def flip(lis, initial, k):
    for i in range(initial, initial + k):
        if lis[i] == '+':
            lis[i] = '-'
        else:
            lis[i] = '+'
    return lis

t = int(input())
n = 1
while n <= t:
    array = input().split(' ')
    s = list(array[0])
    k = int(array[1])
    count = 0
    while True:
        i = ''.join(s).find('-')
        if i == -1:
            print('Case #'+str(n)+': '+str(count))
            break
        if i > (len(s) - k):
            print('Case #'+str(n)+': IMPOSSIBLE')
            break
        else:
            s = flip(s, i, k)
            count += 1
    n += 1
