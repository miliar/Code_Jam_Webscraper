def main():
    with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
        T = input.readline()
        for i in range(1, int(T)+1):
            L = input.readline().split()
            A = int(L[0])
            B = int(L[1])
            y = 0
            if len(L[0]) == 2:
                passes = 0
                for n in range(A, B+1):
                    tens, ones = divmod(n, 10)
                    m = n + (ones - tens) * 9
                    if n < m and m <= B:
                        print '({}, {})'.format(n, m)
                        y += 1
            elif len(L[0]) == 3:
                for n in range(A, B+1):
                    tens, ones = divmod(n, 10)
                    hundreds, tens = divmod(tens, 10)
                    m = n + (ones - hundreds) * 99 + (hundreds - tens) * 9
                    if n < m and m <= B:
                        print '({}, {})'.format(n, m)
                        y += 1
                    m = n + (tens - hundreds) * 99 + (ones - tens) * 9
                    if n < m and m <= B:
                        print '({}, {})'.format(n, m)
                        y += 1

            output.write('Case #' + str(i) + ': ' + str(y) + '\n')

if __name__ == "__main__":
    main()
