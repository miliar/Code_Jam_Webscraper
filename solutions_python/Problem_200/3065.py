import sys

def max_tidy_num(upper):
    right = 0
    while right + 1 < len(upper):
        if upper[right] > upper[right+1]:
            break
        right += 1
    if right + 1 < len(upper):
        # search for leftmost digit equal to i
        left = right
        while left >= 0 and upper[left] == upper[right]:
            left -= 1
        left += 1
        # substract from leftmost
        if upper[left] == 0:
            left -= 1
            upper[left] -= 1
            left += 1
        else:
            upper[left] -= 1
        for i in range(left+1, len(upper)):
            upper[i] = 9
        # remove 0 in the beginning
        if upper[0] == 0:
            upper = upper[1:]
    return ''.join(str(x) for x in upper)

def main(args):
    f = open('B-large.in', 'r')
    o = open('B-large.out', 'w')
    t = int(f.readline())
    for i in range(t):
        test = [int(x) for x in f.readline().strip()]
        print('Case #{0}: {1}'.format(i+1, str(max_tidy_num(test))), file=o)
    f.close()
    o.close()
            
            

if __name__ == '__main__':
    main(sys.argv)