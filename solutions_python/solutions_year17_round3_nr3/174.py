ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(s) for s in input().split(" ")]
    u = float(input())
    pi = [float(s) for s in input().split(" ")]
    pi.sort()
    # print(pi)

    total = sum(pi) + u
    ave = total / len(pi)
    # print(total, ave)
    if ave - max(pi) > -1e-8:
        p = pow(ave, n)
    else:
        used = 0
        i = 0
        eq = 1
        # print(pi)
        while u - used > 1e-8:
            delta = pi[i+1] - pi[i]
            if u - used > delta * eq:
                for j in range(i+1):
                    pi[j] = pi[i+1]
                used += delta * eq
                eq += 1
                i += 1
            else:
                ave_inc = (u-used) / eq
                # print(i)
                for j in range(i+1):
                    pi[j] += ave_inc
                break

        # print(pi)
        p = 1
        for i in pi:
            p *= i


    print("Case #{}: {:.8f}".format(case, p))

