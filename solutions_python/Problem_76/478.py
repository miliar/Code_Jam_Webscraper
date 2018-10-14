from sys import argv, exit

if len(argv) < 3:
    exit("Not enough arguments")

input_file = argv[1]
output_file = argv[2]


def test_patrick_equal(a,b):
    sum_a = 0
    sum_b = 0
    for a1 in a:
        sum_a ^= a1
    for b1 in b:
        sum_b ^= b1
    return sum_a == sum_b



with open(output_file, 'w') as out_desc:
    in_desc = open(input_file)
    num_cases = int(in_desc.readline().strip())
    for t in xrange(num_cases):
        num_candies = int(in_desc.readline().strip())
        candies = sorted(int(i) for i in in_desc.readline().split())
        if test_patrick_equal([candies[0]], candies[1:]):
            print >> out_desc, "Case #%d: %s" % (t+1,sum(candies[1:]))
        else:
            print >> out_desc, "Case #%d: NO" % (t+1)

