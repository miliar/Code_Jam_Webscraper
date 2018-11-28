import sys

def solve(n):
    digits = list(map(int, str(n)))
    sep = 0
    for i in range(len(digits) - 1, 0, -1):
        if(digits[i] < digits[i-1]):
            digits[i-1] -= 1
            sep = i
    if sep == 0:
        return (n,)
    else:
        for i in range(0, len(digits)):
            if i >= sep:
                digits[i] = 9
    return (''.join(map(str, digits)).strip('0'),)



def read_input():
    t = int(input())
    for i in range(t):
        sys.stderr.write('Reading {} out of {}\n'.format(i + 1, t))
        n = int(input())
        yield (n,)


def main():
    results = [solve(*test_case) for test_case in read_input()]
    for i, result in enumerate(results):
        print (
            "Case #{}: {}".format(
                i + 1,
                ' '.join(str(x) for x in result)
            )
        )
if __name__ == '__main__':
    main()