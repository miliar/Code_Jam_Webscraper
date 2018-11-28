def solve(s, n):
    d = {'-': '+',
         '+': '-'}
    ans = 0
    if s.count('-') == 0:
        return 0
    for i in range(len(s)-n+1):
        if s[i] == '-':
            for j in range(n):
                s[i+j] = d[s[i+j]]
            ans += 1
    if '-' in s:
        return 'IMPOSSIBLE'
    else:
        return ans


def main():
    # f = open('A-small-test.txt')
    # f_in = open('A-small-attempt0.in')
    f_in = open('A-large.in')
    # f_out = open('A-small.out', 'w')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for i in range(T):
        s, n = f_in.readline().split()
        f_out.write("Case #{}: {}\n".format(i+1, solve(list(s), int(n))))
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
