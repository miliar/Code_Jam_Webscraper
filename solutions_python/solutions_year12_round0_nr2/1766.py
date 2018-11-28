import sys

def main(args):
    assert len(args) == 2, 'args length != 2: args was %s' % args
    fname = args[1]
    infile = '%s.in' % fname
    outfile = '%s.out' % fname
    
    with open(infile, 'r') as f, open(outfile, 'w') as g:
        num_tests = int(f.readline().strip())
        for i in xrange(1, num_tests+1):
            nums = [int(_) for _ in f.readline().strip().split()]
            num_dancers, num_surprising, threshold = nums[0], nums[1], nums[2]
            scores = sorted(nums[3:], reverse=True)
            if threshold == 0:
                result = num_dancers
            elif threshold == 1:
                result = sum(1 for score in scores if score > 0)
            else:
                result = 0
                int_result = 0
                for score in scores:
                    if score > (threshold * 3 - 3):
                        result += 1
                    elif (threshold * 3 - 4) <= score <= (threshold*3-3):
                        int_result += 1
                result += min(int_result, num_surprising)
            g.write('Case #%s: %s\n' % (i, result))
    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
