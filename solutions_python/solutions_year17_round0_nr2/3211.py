t = int(raw_input())

for i in xrange(t):
    val = 0
    n = raw_input().strip()
    if len(n) == 1:
        val = int(n)
    else:
        works = False
        while not works:
            n_list = [int(x) for x in n]
            l = len(n_list)
            found = False
            for j in xrange(1, l):
                if n_list[j] < n_list[j-1]:
                    n = n[:j-1] + str(n_list[j-1] - 1) + '9'*(l-j)
                    found = True
                    break
            if not found:
                works = True
                val = int(n)
    print("Case #{}: {}".format(i+1, val))