import fileinput


def solve(n):
    l = len(n)
    # One digit is always "tidy"
    if l == 1:
        return n
    for i in range(l - 1):
        if n[i] > n[i + 1]:
            j = i
            while j > 0 and n[j - 1] == n[j]:
                j -= 1
            return n[:j] + chr(ord(n[j]) - 1) + '9' * (l - j - 1)
    return n


if __name__ == '__main__':
    stdin = fileinput.input()
    nprobs = int(next(stdin).strip())
    for n in range(1, nprobs + 1):
        print("Case #%d:" % n, int(solve(next(stdin).strip())))
