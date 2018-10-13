def init():
    a, b = raw_input().split(' ')
    return int(a), int(b)

def transform(a, b):
    oriA = str(a)
    oriB = str(b)
    # print a, b
    for i in range(1, len(oriA)):
        newA = oriA[i:] + oriA[:i]
        # print newA
        if newA == oriB:
            return True
    return False

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        count = 0
        a, b = init()
        for i in range(a, b+1):
            for j in range(i+1, b+1):
                if transform(i, j):
                    count += 1
        print 'Case %d#: %d' % (t+1, count)
