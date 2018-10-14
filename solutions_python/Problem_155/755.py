'''
Created on April 12, 2014

@author: Lior
'''

def solve(s):
    answer = 0
    for shyness, ll in enumerate(s):
        i = int(ll)
        if shyness == 0:
            so_far = i
            continue

        if so_far >= shyness:
            so_far += i
        else:  # not enough!
            new_invitees = shyness - so_far
            answer += new_invitees 
            so_far += new_invitees + i
    return answer

def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        digits, s = in_file.next().strip().split(' ')
        assert int(digits) + 1 == len(s)
        result = solve(s)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))

if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
