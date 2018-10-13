def empty(s):
    for x in s:
        if x != '?':
            return False
    return True


def fill(s):
    p = ''
    last = ''
    first = ''
    count = 0
    for x in s:
        if last == '':
            if x == '?':
                count += 1
            else:
                first = x
                p += x
                last = x
        else:
            if x != '?':
                last = x
            p += last
    return count * first + p

T = int(input())
for tid in range(T):
    a = []
    R, C = [int(x) for x in input().split(' ')]
    for r in range(R):
        s = input()
        a.append(s)
    b = []
    last = ''
    first = ''
    count = 0
    for r in a:
        if last == '':
            if not empty(r):
                last = fill(r)
                first = last
                b.append(last)
            else:
                count += 1
        else:
            if not empty(r):
                last = fill(r)
            b.append(last)
    for i in range(count):
        b.insert(0,first)

    print('Case #{}:'.format(tid + 1))
    for x in b:
        print(x)
