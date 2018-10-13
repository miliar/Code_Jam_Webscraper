def print_flips(case_no, s, k):
    ls = list()
    front = 0
    for i in xrange(len(s)-k+1):
        if len(ls) > front and ls[front] + k <= i:
            front += 1
        if s[i] == '-' and (len(ls)-front) % 2 == 0:
            ls.append(i)
        elif s[i] == '+' and (len(ls)-front) % 2 == 1:
            ls.append(i)
        

    done = True
    for i in xrange(len(s)-k+1, len(s)):
        if len(ls) > front and ls[front] + k <= i:
            front += 1
        if s[i] == '-' and (len(ls)-front) % 2 == 0:
            done = False
        elif s[i] == '+' and (len(ls)-front) % 2 == 1:
            done = False
        

    if done:
        print "Case #{0}: {1}".format(case_no+1, len(ls))
    else:
        print "Case #{0}: IMPOSSIBLE".format(case_no+1)


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(0, t):
        s, k_str = raw_input().split(" ")
        k = int(k_str)
        print_flips(i, s, k)
