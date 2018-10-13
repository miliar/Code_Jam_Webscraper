t = int(raw_input())

for j in range(t):
    n = int(raw_input())
    while True:
        n_digits = map(int, str(n))
        tidy_el = True
        for i in range(len(n_digits)-2, -1, -1):
            if n_digits[i+1] < n_digits[i]:
                tidy_el = False
                s = 1
                for m in range(len(n_digits)-1, i, -1):
                    s += (10**(len(n_digits)-m-1))*n_digits[m]
                n -= s
                break
        if tidy_el:
            print "Case #{0}: {1}".format(j+1, n)
            break
