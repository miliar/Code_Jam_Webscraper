def closest_two(num):
    ret = 1
    while ret <= num:
        ret *= 2
    return ret/2

def bathroom(N,K):

    two_pow = closest_two(K)

    people_left = K - two_pow + 1

    toilets_left = N - two_pow + 1

    big_spaces = toilets_left % two_pow

    space_size = toilets_left / two_pow

    if people_left <= big_spaces:
        space_size += 1

    return str((space_size)/2) + ' ' + str((space_size-1)/2)

t = int(raw_input())

for x in xrange(1, t+1):
    N,K = raw_input().split(' ')
    N, K = int(N), int(K)
    print 'Case #{}: {}'.format(x, bathroom(N,K))