import sys

f = open(sys.argv[1], 'r')
num_lines = int(f.readline())

def run_case(data, extra=0):
    standing = extra
    for shyness, count in enumerate(data):
        if standing < shyness:
            return False
        else:
            standing += count
    return True


for num in range(1, num_lines + 1):
    data = f.readline().strip().split(' ')
    nums = list(map(lambda s: int(s), data[1]))

    extra = 0
    while True:
        if run_case(nums, extra):
            print("Case #%d: %d" % (num, extra))
            break
        else:
            extra += 1
