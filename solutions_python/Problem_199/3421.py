if __name__ == '__main__':
    t = int(input().strip())
    for tests in range(1, t + 1):
        s, k = input().split()
        k = int(k)
        s = s.strip()
        if k > len(s):
            answer = "IMPOSSIBLE"
        else:
            tr = 0
            flag = False
            i = 0
            while i <= len(s) - k:
                if s == '+' * len(s):
                    flag = True
                    break
                if s[i] == '+':
                    i += 1
                    continue
                tr += 1
                for j in range(0, k):
                    flip = '-' if s[i+j] == '+' else '+'
                    A = list(s)
                    A[i+j] = flip
                    s = ''.join(A)
                i += 1
            if s == '+' * len(s):
                flag = True
            answer = tr if flag else "IMPOSSIBLE"
        print("Case #{test}: {ans}".format(test=tests, ans=answer))