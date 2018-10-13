import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

NO_RESULT = "NO"

def is_mod2_equally_splitable(values):
    mod2_sum = 0
    for value in values:
        mod2_sum ^= value
    return not bool(mod2_sum)

def get_mod2_equal_parts(values):
    values = values[:]
    values.sort()
    large_part = 0
    for value in values[1:]:
        large_part += value
    return (values[0], large_part)
    
def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            candy_num = int(input_f.readline())
            candy_values = [int(x) for x in input_f.readline().strip().split(" ")]
            
            result = None
            if (is_mod2_equally_splitable(candy_values)):
                (patrick_share, sean_share) = get_mod2_equal_parts(candy_values)
                result = sean_share
            else:
                result = NO_RESULT
                            
            output_f.write("Case #%d: %s\n" % (test_case_i + 1, result))
    
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
