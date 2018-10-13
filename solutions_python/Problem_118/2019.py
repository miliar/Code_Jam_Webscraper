def read_input_file(filename = "A-small.in"):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    T = int(lines[0])
    cases = []
    #for i in range(N):
    #    cases.append(#[list containing all information for each case])
    return T, cases

def create_output(filename = "A_solution.txt", answer_list):
    file = open(filename, 'w')
    for i in range(len(answer_list)):
        print "Case #%d: %s" % (i+1, answer_list[i])
        output = "Case #%d: %s\n" % (i+1, answer_list[i])
        file.write(output)
    file.close()

T, cases = read_input_file("test.in")

results = []

#for case in cases:
#    get data out of case into variables
#    solve case
#    results.append(#print string of solved case)

create_output("testsol.txt")

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

da = {}

for i in range(10000000):
    if is_palindrome(i):
        s = i * i
        if is_palindrome(s):
            print "found", s; da[s] = True


def create_output(filename, cases):
    file = open(filename, "w")
    for i in range(len(cases)):
        print "Case #%d: %s" % (i+1, do_it(*cases[i]))
        output = "Case #%d: %s\n" % (i+1, do_it(*cases[i]))
        file.write(output)
    file.close()

def read_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    T = int(lines[0])
    cases = []
    for line in lines[1:]:
        start, end = line.split()
        start = int(start)
        end = int(end)
        cases.append((start, end))
    return cases


