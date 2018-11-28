import gmpy
import itertools

def solve(N, numbers):
    diff = [abs(a - b) for a, b in itertools.product(numbers, numbers)]
    gcd = reduce(gmpy.gcd, diff, 0)
    result = (gcd - (numbers[0] % gcd)) % gcd
    return result

def main():
    file = open('B-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        numbers = [int(x) for x in file.readline().split()]
        N, numbers = numbers[0], numbers[1:]
        print >> output, 'Case #%d:' % case, solve(N, numbers)
    output.close()
    
if __name__ == '__main__':
    main()
    
