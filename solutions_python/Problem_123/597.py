
def main():
    num_of_tests = int(raw_input())
    for test_i in range(num_of_tests):
        A, N = map(int, raw_input().split(' '))
        a = map(int, raw_input().split(' '))
        a.sort()
        max_size = max(a) + 1
        d1 = [N + 1 for i in range(max_size + 1)]
        d1[min(A, max_size)] = 0
        for i in range(N):
            d2 = [N + 1 for k in range(max_size + 1)]
            for j in range(1, max_size + 1):
                if d1[j] > N: continue
                d2[j] = min(d2[j], d1[j] + 1)
                if a[i] < j:
                    x = min(j + a[i], max_size)
                    d2[x] = min(d2[x], d1[j])
                elif j > 1:
                    n_op = 0
                    x = j
                    while x <= a[i]:
                        n_op += 1
                        x += x - 1
                    x = min(x + a[i], max_size)
                    d2[x] = min(d2[x], d1[j] + n_op)
            d1 = d2
        ans = min(d2)
        print "Case #%d: %s" % (test_i + 1, ans)

if __name__ == "__main__":
    main()
