def main():
    fout = open("output", "w")
    with open("input", "r") as fin:
        T = int(fin.readline())
        for testcase in range(1, T + 1):
            name, n = fin.readline().split()
            n = int(n)
            result = 0
            first = 0
            vowels = ['a', 'e', 'i', 'o', 'u']
            # current_len = 0 if name[0] in vowels else 1
            current_len = 0
            for last in range(len(name)):
                if name[last] in vowels:
                    current_len = 0
                else:
                    current_len += 1
                if current_len >= n:
                    result += (len(name) - last) * (last - n - first + 2)
                    first = last - n + 2
            print >> fout, "Case #%d: %d" % (testcase, result)


if __name__ == '__main__':
    main()
