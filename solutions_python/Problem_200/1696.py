maps = {
    '1':'0',
    '2':'1',
    '3':'2',
    '4':'3',
    '5':'4',
    '6':'5',
    '7':'6',
    '8':'7',
    '9':'8',
}
def Solution(label, line):
    pivot = list(line)
    last = len(line) - 1 # last digit behind this one all 9's
    for i in xrange(-1,-(len(pivot)), -1):
        if pivot[i-1] > pivot[i]:
            pivot[i-1] = maps[pivot[i-1]]
            last = i - 1 + len(line)
    for i in range(last+1, len(line)):
        pivot[i] = '9'
    number = ''.join(pivot)
    number = int(number)

    print "Case #{}: {}".format(label, number)
    return 1


if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            out = Solution(i, line)