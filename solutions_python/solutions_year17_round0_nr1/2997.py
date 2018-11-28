def result(s, k):
    k = int(k)
    flips = 0
    bits = [1 if x == '+' else 0 for x in s]
    for i in range(len(bits)):
        if bits[i] == 0:
            if i + k > len(bits):
                return 'IMPOSSIBLE'
            flips += 1
            for j in range(k):
                bits[i+j] = 1 - bits[i+j]
    return flips


if __name__ == "__main__":
    FILE_NAME = 'A-large'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()

            for i in range(len(r) - 1):
                w.write('Case #%d: %s\n' % (i + 1, result(*r[i + 1].split())))