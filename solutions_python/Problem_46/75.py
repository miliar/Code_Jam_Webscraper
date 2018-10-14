def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def readString():
    r = raw_input()
    return r

def count(st):
    loc = []
    for i in range(len(st)):
        loc.append(st[i].rfind('1'))

    # print loc

    count = 0
    length = len(st)
    for i in range(length):
        if loc[i] > i:
            for j in range(i, length):
                if loc[j] <= i:
                    break
            for k in range(j, i, -1):
                tmp = loc[k]
                loc[k] = loc[k - 1]
                loc[k - 1] = tmp
                count += 1

    # print st
    return count

def main():
    t = readInts()[0]

    case = 1
    for i in range(t):

        n = readInts()[0]
        st = []

        for j in range(n):
            st.append(readString())

        print 'Case #%d: %d' % (case, count(st))
        case += 1

if __name__ == '__main__':
    main()
