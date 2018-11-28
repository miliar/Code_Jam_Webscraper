def output_answer(case_number, answer, line):
    output = 'Case #%i: %i' % (case_number, answer)
    print '%s (for %s)' % (output, line.strip())
    return output


def get_answer(line):
    max_shyness, audience = line.split(' ')
    audience = audience.strip()
    current_num_clappers = int(audience[0])
    friends_needed = 0
    for num_clappers_needed in xrange(1, len(audience)):
        num_clappers_needed = int(num_clappers_needed)
        if current_num_clappers >= num_clappers_needed:
            current_num_clappers += int(audience[num_clappers_needed])
        else:
            additional_friends = (num_clappers_needed - current_num_clappers)
            friends_needed += additional_friends
            current_num_clappers += (additional_friends + int(audience[num_clappers_needed]))
    return friends_needed


def output_answers(attempt=0):
    base_filename = 'A-large'
    infilename = base_filename + '.in'
    outfilename = base_filename + '.out'

    infile = open(infilename, 'r')
    outfile = open(outfilename, 'w')

    num_cases = int(infile.readline())

    for ith_case in xrange(1, num_cases + 1):
        line = infile.readline()
        #output_answer(ith_case, -1, line)
        answer = get_answer(line)
        output = output_answer(ith_case, answer, line)
        outfile.write(output + '\n')

if __name__ == '__main__':
    output_answers()
