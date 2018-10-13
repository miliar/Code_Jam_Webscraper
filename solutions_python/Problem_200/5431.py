def Tidy(T, inputs):
    for t in range(T):
        [N] = inputs[t]
        for n in [N]:
            n = int(n)
            nums = list(range(1, n+1))
            for num in nums:
                d = list(map(int, str(num)))
                sd = sorted(d, key = int)
                if d == sd:
                    nm = int(''.join(map(str, d)))
                    output = 'Case #' + str(t+1) + ":  " + str(nm) + '\n'
            print(output)
            with open('stdout.txt',  'a') as of:
                of.write(output)
    of.close()


def main():
    with open("B-small-attempt3.in", 'r') as f:
        content = f.readlines()
        T = int(content[0])
        inputs = list(map(lambda l : l.strip().split(' '), content[1:]))
    Tidy(T, inputs)


if __name__ == '__main__':
    main()
