import math


if __name__ == '__main__':
    infile = open('data.in', 'rb')
    num_cases = int(infile.readline())
    for case_num in range(1, num_cases + 1):
        low, high = map(int, infile.readline().split())
        low_root = int(math.ceil(math.sqrt(low)))
        high_root = int(math.floor(math.sqrt(high)))
        num_fair = 0
        for x in range(low_root, high_root + 1):
            sx = str(x)
            if sx != sx[::-1]:
                continue
            x2 = x * x
            sx2 = str(x2)
            if sx2 == sx2[::-1]:
                num_fair += 1
        result = str(num_fair)
        print 'Case #%d: %s' % (case_num, result)
