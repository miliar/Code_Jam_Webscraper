

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n, k = [int(s) for s in raw_input().split(" ")]
        a, b = stall(n, k)
        print "Case #{}: {} {}".format(i, a, b)

def stall(n, k):
    d = {n:1}
    answer = []
    if n == k:
        return (0, 0)
    for i in xrange(k):
        key = max(d)
        if key % 2 == 1:
            if (key-1)/2 not in d:
                d[(key-1)/2] = 2
            else:
                d[(key-1)/2] += 2
            answer = [(key-1)/2]*2
        elif key % 2 == 0:
            if key / 2 not in d:
                d[key/2] = 1
            else:
                d[key/2] += 1
            if (key / 2)-1 not in d:
                d[(key / 2)-1] = 1
            else:
                d[(key / 2)-1] += 1
            answer = [key / 2, (key / 2)-1]
        d[key] -= 1
        if d[key] == 0:
            d.pop(key)
    return answer[0], answer[1]

def maximum_zero(l):
    maximum,index = l[0], 0
    for i in xrange(len(l)):
        if l[i] > 0:
            maximum = l[i]
            index = i
            break
    return maximum, index

if __name__ == '__main__':
    main()
