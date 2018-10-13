import sys
import math

with open(sys.argv[1]) as f:
    looper = int(f.readline())
    case = 0
    while looper > 0:
        case +=1
        looper -= 1

        a, b = [int(x) for x in filter(lambda g: g != '\n', f.readline()).split(' ')]

        fs_count = 0
        for num in range(a, b+1):
            num_str = str(num)
            if num_str == num_str[::-1]:
                num_sqrt = math.sqrt(num)
                if num_sqrt.is_integer():
                    num_sqrt_str = str(int(num_sqrt))
                    if num_sqrt_str == num_sqrt_str[::-1]:
                        fs_count += 1
        print 'Case #{0}: {1}'.format(case, fs_count)