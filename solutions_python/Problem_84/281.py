import sys

def solve(testcase):
    h = len(testcase)
    w = len(testcase[0])
    
    doneSomething = True
    
    while doneSomething:
        doneSomething = False
        
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                if  testcase[y-1][x-1] != "#" and testcase[y-1][x-0] != "#" and \
                    testcase[y-0][x-1] != "#" and testcase[y-0][x-0] == "#":
                
                    if  testcase[y-0][x-0] == "#" and testcase[y-0][x+1] == "#" and \
                        testcase[y+1][x-0] == "#" and testcase[y+1][x+1] == "#":
                    
                        testcase[y-0][x-0] = "/"
                        testcase[y-0][x+1] = "\\"
                        testcase[y+1][x-0] = "\\"
                        testcase[y+1][x+1] = "/"
                        
                        doneSomething = True
        
    
    if ("#" in "".join(["".join(line) for line in testcase])):
        print("Impossible")
    else:
        for i in testcase[1:-1]:
            print("".join(i[1:-1]))
                
    
    
def read_line(file_desc):
    return [int(i) for i in file_desc.readline().split()]

def parseInput(fn):
    f = open(fn, "r")
    test_cases = read_line(f)[0]
    
    for i in range(test_cases):
        h, w = read_line(f)
        testcase = []
        
        testcase.append(["."] * (w+2))
    
        for y in range(h):
            testcase.append(["."] + list(f.readline().strip()) + ["."])
        
        testcase.append(["."] * (w+2))
 
        print("Case #%d:" % (i+1))
        solve(testcase)

#parseInput("in1.txt")

out =  open("A-large.out", "w")

sys.stdout = out

parseInput("A-large.in")
#input()