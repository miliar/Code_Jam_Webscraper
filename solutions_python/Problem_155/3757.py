'''
An attempted solution for Google CodeJam 2015,
Qualifying round, Problem A

AUTHOR
    Yoshua Wakeham
    yoshwakeham@gmail.com

'''
import sys

def get_test_cases():
    '''
    Read test case input file.
    '''
    if len(sys.argv) != 2:
        print("Usage error")
        sys.exit()
    input_fname = sys.argv[1]
    test_cases = []
    with open(input_fname) as infile:
        num_cases = infile.next()
        for i in range(int(num_cases)):
            test_cases.append(infile.next())
    return test_cases

def ovation_invites(testcase):
    '''
    Testcase is a string of the form
    maxSi n0n1n2n3n4...
    '''
    max_shyness, count_string = testcase.split()
    shy_counts = map(int, list(count_string))
    num_standers = 0
    num_invites = 0
    for i in range(int(max_shyness)+1):
        if shy_counts[i] == 0:
            continue
        else:
            if num_standers < i:
                num_invites += i - num_standers
                num_standers += num_invites
            num_standers += shy_counts[i]
    return num_invites

if __name__ == '__main__':
    cases = get_test_cases()

    with open('output.out', 'w') as f:
        for i in range(len(cases)):
            soln = ovation_invites(cases[i])
            output_line = "Case #{}: {}\n".format(i+1, soln)
            f.write(output_line)
