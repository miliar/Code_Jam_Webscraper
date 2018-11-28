def main():
    inp = open('A-large.in', 'r')
    output = open('output2.txt', 'w')
    n = int(inp.readline())
    for i in range(n):
        a = inp.readline()
        a = a.split()
        a[0] = int(a[0])
        Sum = 0
        inv = 0
        for j in range(a[0] + 1):
            if Sum < j:
                inv += j - Sum
                Sum = j
            Sum += int(a[1][j])
        print('Case #%d: %d'% (i + 1, inv), file = output)
    inp.close()
    output.close()
if __name__ == '__main__':
    main()
