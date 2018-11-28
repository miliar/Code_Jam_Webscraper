def solve(R, B, Y):
    if B + Y < R:
        return 'IMPOSSIBLE'
    if Y + R < B:
        return 'IMPOSSIBLE'
    if R + B < Y:
        return 'IMPOSSIBLE'
    M1, M3 = max(R, B, Y), min(R, B, Y)
    M2 = R + B + Y - M1 - M3

    seq = []
    while M1:
        seq.append(1)
        M1 -= 1
        if M2 >= M3:
            seq.append(2)
            M2 -= 1
            lastM2 = True
        else:
            seq.append(3)
            M3 -= 1
            lastM2 = False
    while M2 or M3:
        if lastM2:
            seq.append(3)
            M3 -= 1
            lastM2 = False
        else:
            seq.append(2)
            M2 -= 1
            lastM2 = True
    if max(R, B, Y) == R:
        seq = ['R' if s == 1 else s for s in seq]
        if min(R, B, Y) == B:
            seq = ['B' if s == 3 else s for s in seq]
            seq = ['Y' if s == 2 else s for s in seq]
        else:
            seq = ['B' if s == 2 else s for s in seq]
            seq = ['Y' if s == 3 else s for s in seq]
    elif max(R, B, Y) == B:
        seq = ['B' if s == 1 else s for s in seq]
        if min(R, B, Y) == R:
            seq = ['R' if s == 3 else s for s in seq]
            seq = ['Y' if s == 2 else s for s in seq]
        else:
            seq = ['R' if s == 2 else s for s in seq]
            seq = ['Y' if s == 3 else s for s in seq]
    else:
        seq = ['Y' if s == 1 else s for s in seq]
        if min(R, B, Y) == R:
            seq = ['R' if s == 3 else s for s in seq]
            seq = ['B' if s == 2 else s for s in seq]
        else:
            seq = ['B' if s == 3 else s for s in seq]
            seq = ['R' if s == 2 else s for s in seq]
    return ''.join(seq)
        

def main(index):
    print 'Case #%d:' % index,
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    print solve(R, B, Y)

T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
