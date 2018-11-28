#! /usr/bin/pypy

vowels = "aeiou"

def helper(name,index,n):
    for i in range(n):
        if name[index+i] in vowels:
            return False
    return True

def solve(name,n):
    if len(name) < n:
        return 0

    name_len = len(name)
    n_groups_len = len(name)-n+1
    n_groups = [n_groups_len-i if helper(name,i,n) else 0
        for i in range(n_groups_len)
        ]

    last_thingy = 0
    the_sum = 0
    for i in reversed(range(len(n_groups))):
        if n_groups[i] != 0:
            last_thingy = n_groups[i]
        the_sum += last_thingy

    return the_sum

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases in the first line
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for i,line in enumerate(f.readlines()):
        name, n =  line.split(" ") #split one line, convert to int
        n = int(n)

        a = "Case #%s: %s"%(i+1,solve(name,n)) #solution line
        solutions.append(a)
        print a

    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

if __name__ == "__main__":
    # something which needs to be precomputed goes here

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
