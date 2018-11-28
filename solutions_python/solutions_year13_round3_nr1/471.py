import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def does_have_n_consonants(substr, n):
    consec_cons = 0
    for char in substr:
        if char in vowels:
            consec_cons = 0
        else:
            consec_cons += 1
        if consec_cons >= n:
            return True
    return False

def does_have_consonants(substr):
    for char in substr:
        if char in vowels:
            return False
    return True

def solve_naive(name, n):
    number_of_substrs = 0
    for first_idx in range(len(name)-n + 1):
        for last_idx in range(len(name), n-1, -1):
            if last_idx - first_idx < n:
                continue
            if does_have_n_consonants(name[first_idx:last_idx], n):
                number_of_substrs += 1
    return number_of_substrs

def process_files(in_file, out_file):
    tc_count = in_file.readline()
    for tc_idx in range(0, int(tc_count)):
        name, n =  in_file.readline().strip().split()
        sys.setrecursionlimit(1500)
        
        out_file.write('Case #%d: ' % (tc_idx+1))
        print('Case #%d:' % (tc_idx+1))
        #print(solve_naive(name, int(n)))
        
        
        #print('Case #%d:' % (tc_idx+1))
        
        out_file.write("{0}".format(solve_naive(name, int(n))))
        out_file.write("\n")
        
if __name__ == '__main__':
    with open('A-small-attempt0.in', 'rb') as in_file:
        with open('output.txt', 'wb') as out_file:
            process_files(in_file, out_file)