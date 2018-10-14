def solve():
    a = list(input())[::-1]
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            a[i] = str(int(a[i]) - 1)
            a[:i] = ['9'] * i
    if a[-1] == '0':
        a.pop()
    return ''.join(a[::-1])

def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {}'.format(test, solve()))

if __name__ == '__main__':
    main()
