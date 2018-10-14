
def dancing(fh_in, fh_out):

    test_cases = int(fh_in.readline())

    for case_count in range(test_cases):

        details = fh_in.readline()
        _, surprises, target, scores = details.split(" ", 3)

        target = int(target)
        surprises = int(surprises)
        reached_target = 0
        for s in scores.split(" "):
            s = int(s)

            base_score = s/3 # Min score received by any judge
            remainder = s%3 # Remainder


            if base_score >= target:
                reached_target += 1
            elif base_score == target - 1:
                if remainder:
                    reached_target += 1
                elif surprises and s > 1:
                    reached_target += 1
                    surprises -= 1
            elif base_score == target - 2 and remainder == 2 and surprises:
                reached_target += 1
                surprises -= 1

        fh_out.write("Case #%i: %i\n"%(case_count+1, reached_target))


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

    dancing(fh_in, fh_out)