# Zolmeister

T = int(raw_input())

def is_sorted(N):
    return all(N[i] <= N[i+1] for i in xrange(len(N)-1))

# Simple
# for t in xrange(T):
#     N = int(raw_input())
#
#     while not is_sorted(str(N)):
#         N -= 1
#         print N
#
#     print 'Case #{}: {}'.format(t + 1, str(N))

def sub_one(N, i = -1, skip_9 = False):
    if N[i] == 9 and not skip_9:
        sub_one(N, i - 1)
    elif N[i] == 0:
        N[i] = 9
        sub_one(N, i - 1, True)
    else:
        N[i] -= 1

for t in xrange(T):
    N = map(int, list(raw_input()))

    while not is_sorted(N):
        sub_one(N)

    i = 0
    while N[i] == 0:
        N[i] = ''
        i += 1

    print 'Case #{}: {}'.format(t + 1, ''.join(map(str, N)))
