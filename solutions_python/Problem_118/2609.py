import math

def palindrom(string):
    n = len(string)
    for i in xrange(n / 2 + 1):
        if string[i] != string[n - 1 - i]:
            return False
    return True

def main():
    filename = 'C-small-attempt0.in'
    input = open(filename, 'r')

    tests_count = int(input.readline().strip())

    output = open('C-small-attempt0.out', 'w')

    for case in xrange(tests_count):
        ans = 0

        a, b = map(int, input.readline().strip().split())

        for x in xrange(a, b + 1):
            sqx = math.sqrt(x)
            if sqx.is_integer() and palindrom(str(int(sqx))) and palindrom(str(x)):
                ans += 1

        output.write('Case #{0}: {1}\n'.format(case + 1, ans))

    output.close()

if __name__ == '__main__':
    main()
