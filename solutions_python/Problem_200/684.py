__author__ = 'snv'


# sys.setrecursionlimit(10001)


f = open('B-large.in','r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    last_num = int(f.readline().strip())
    digits = [int(k) for k in str(last_num)]
    # print(digits)
    prev = 0
    tidy = []
    is_non_tidy = False
    for digit in digits:
        if is_non_tidy:
            tidy.append(9)
            continue
        if digit >= prev:
            tidy.append(digit)
            prev = digit
        else:
            is_non_tidy = True
            if prev > 1:
                first_prev = min( i for i in range(len(tidy)) if tidy[i]== prev)
                tidy[first_prev] = prev -1
                for i in range(first_prev+1, len(tidy)):
                    tidy[i] = 9
            else:
                tidy = [9 for d in tidy[1:]]
            tidy.append(9)

    ans = ''.join([str(d) for d in tidy])

    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

