def solve(N):
    ans = 1
    for i in range(N+1):
        if i == int(''.join(sorted(str(i)))):
            ans = max(ans, i)
    return ans


def main():
    # f_in = open('B-small-test.in')
    f_in = open('B-small-attempt0.in')
    # f_in = open('B-large.in')
    f_out = open('B-small.out', 'w')
    # f_out = open('B-large.out', 'w')
    T = int(f_in.readline())
    for i in range(T):
        N = int(f_in.readline())
        f_out.write("Case #{}: {}\n".format(i+1, solve(N)))
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
