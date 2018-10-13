1000


def test_case():
    N = int(input())
    digits = [ int(d) for d in reversed(str(N)) ]
    for i in range(len(digits)):
        if i + 1 < len(digits) and digits[i] < digits[i + 1]:
            j = i - 1
            while j >= 0:
                digits[j] = 9
                j -= 1
            digits[i] = 9
            digits[i + 1] -= 1

    return int(''.join(map(str, reversed(digits))))

def main():
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t + 1), test_case())

if __name__ == '__main__':
    main()
