
def recycled_numbers(fh_in, fh_out):

    test_cases = int(fh_in.readline())

    for case_count in range(test_cases):
        details = fh_in.readline()
        lower, upper = details.split(" ")

        l = int(lower)
        u = int(upper)

        count = 0
        seen = {}
        for num in range(l, u):
            num_str = str(num)
            for j in range(1, len(num_str)):
                recycled = "%s%s"%(num_str[-j:], num_str[:-j])

                if recycled[0] != '0' and l <= num < int(recycled) <= u:
                    seen_str = '%s#%s'%(num_str, recycled)
                    seen_str2 = '%s#%s'%(recycled, num_str)

                    if seen_str not in seen and seen_str2 not in seen:
                        count += 1
                    seen[seen_str] = 1
                    seen[seen_str2] = 1

        fh_out.write("Case #%i: %i\n"%(case_count+1, count))



if __name__ == '__main__':

    # Validate command line args
    import sys
    import os

    args = sys.argv
    if len(args) != 2:
        raise Exception("Single filename argument required")

    input_filename = args[1]
    output_filename = "%s.out"%(os.path.splitext(input_filename)[0])
    fh_in = open(input_filename)
    fh_out = open(output_filename, 'w')

    recycled_numbers(fh_in, fh_out)