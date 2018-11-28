def numbers(a, b):
    n = 0

    for i in xrange(a, b+1):
        found = []
        s = str(i)
        for j in xrange(len(s)):
            new_s = s[j:] + s[:j]
            new_i = int(new_s, 10)
            if (i < new_i and new_i <= b and 
                len(str(i)) == len(str(new_i)) and new_i not in found):
                n += 1
                found.append(new_i)
    return n

#print numbers(1111, 2222)
if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        ns = map(int, raw_input().split(' '))
        print "Case #%d: %d" % (i+1, numbers(ns[0], ns[1]))
