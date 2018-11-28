# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def load_file(filename):
    in_file = open(filename, encoding='utf-8')
    content = in_file.readlines()
    return content

def writeStringToFile(output, filename):
    out_file = open(filename + '.out', 'w')
    for i in output:
        out_file.write(i + '\n')
    out_file.close()

def flipk(k, stack, i):
    #print("before", k, stack, i)
    size = len(stack)
    new_stack = stack[:i - k]
    for j in range(k):
        if stack[i - k + j] == '-':
            new_stack += '+'
        else:
            new_stack += '-'
    new_stack += stack[i:size]
    #print("after", new_stack)
    return new_stack

def allFlipped(stack, size):
    for i in range(size):
        if stack[i] == '-':
            return False
    return True
   
def solve(line):
    stack, K = line.split()[0], int(line.split()[1])
    size = len(stack)
    count = 0
    for i in range(size - K + 1):
        if stack[size - i - 1] == '-':
            stack = flipk(K, stack, size - i)
            count += 1
    if allFlipped(stack, size):
        return count
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    filename = "A-large.in"
    file = load_file(filename)
    n = int(file[0])
    #print(int(file[0]))
    out = []
    for i in range(1, n+1):
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
#print(out)
writeStringToFile(out, filename)


#def load_file(filename):
#    in_file = open(filename, encoding='utf-8')
#    test_cases = in_file.readline().strip().split()
#    print(test_cases)
#    cases_data = []
#    for i in range(test_cases):
#        cases_data.append(list(in_file.readline().strip()))
#    in_file.close()
#    return test_cases, cases_data
#

#
## Read a file
#test_cases, cases_data = load_file("A-small.in")
#out = []
#MAX_ITER = 10
#
#for i in range(MAX_ITER):
#  print(i)
#  out.append("Case #{}: {} {}".format(i, i, i)) 
#print(out)
#writeStringToFile("A-small.out")