with open('B-large.in', 'r') as f_in, open('out.txt', 'w') as f_out:
    t = int(f_in.readline())
    for i_, k in enumerate(f_in):
        k = k.rstrip()  # last char in k could be a '\n'
        k = [int(x) for x in k]
        # print("Case #{}: {}".format(i_ + 1, k))

        flag = True
        while flag:
            flag = False
            for i in range(len(k)-1):
                if k[i] > k[i+1]:
                    assert k[i] != 0
                    k[i] -= 1
                    n = len(k[i+1:])
                    del k[i+1:]
                    k.extend([9] * n)
                    flag = True
                    # print("         {}".format(k))

        k = int(''.join([str(x) for x in k]))
        f_out.write("Case #{}: {}\n".format(i_ + 1, int(k)))
