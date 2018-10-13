def solve_candies(elements):
    total = reduce(int.__xor__, elements)
    if total:
        return "NO"
    return str(sum(elements) - min(elements))

if __name__ == '__main__':
    number_of_tests = int(raw_input())
    for t in range(1, number_of_tests+1):
        n = int(raw_input())
        elements = [int(k) for k in raw_input().split(' ')]
        answer = solve_candies(elements)
        print 'Case #%d: %s' % (t, answer)
