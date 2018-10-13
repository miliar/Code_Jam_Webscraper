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

def isTidy(string):
    size = len(string)
    isTidy = True
    diff = 0
    for i in range(size - 1):
        if string[i] > string[i + 1]:
            isTidy = False
            diff = int(string[i + 1:]) + 1
    return isTidy, diff

def decreased(string, diff):
    return str(int(string) - diff)

def solve(line):
    string = line.split()[0]
    tidy, diff = isTidy(string)
    while not tidy:
        string = decreased(string, diff)
        tidy, diff = isTidy(string)
    return string

if __name__ == "__main__":
    filename = "B-large.in"
    file = load_file(filename)
    n = int(file[0])
#    print(int(file[0]))
    out = []
    for i in range(1, n+1):
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
#print(out)
writeStringToFile(out, filename)
