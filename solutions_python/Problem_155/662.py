
def main():
    for case in range(int(input())):
        m = map(int, list(input().split()[1]))
        a = list(m)
        s = 0
        result = 0
        for i in range(len(a)):
            if i > s:
                result += i - s
                s = i
            s += a[i]

        print('Case #%d: %s' % (case + 1, result))

if __name__ == "__main__":
    main()
