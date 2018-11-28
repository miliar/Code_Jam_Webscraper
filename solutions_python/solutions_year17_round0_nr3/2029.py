import math

def stalls(n, k):
    sections = 2**math.floor(math.log2(k))
    taken = sections - 1

    remaining = n - taken

    section_length = int(remaining / sections)
    extras = remaining % sections

    place_in_section = k - sections

    L = int(section_length / 2)
    R = int(section_length / 2)

    if section_length % 2 == 0:
        L -= 1

    if place_in_section < extras:
        L += 1

    return (max(L, R), min(L, R))


t = int(input())
for i in range(1, t + 1):
    line = input().split(' ')
    N = int(line[0])
    K = int(line[1])

    result = stalls(N, K)
    maxLR = result[0]
    minLR = result[1]

    print('Case #{}: {} {}'.format(i, maxLR, minLR))