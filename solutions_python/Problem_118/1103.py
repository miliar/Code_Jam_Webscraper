import copy
import math


max_height = 100

def readLineOfInts(fin):
    return [int(x) for x in fin.readline().strip().split()]

def importData(filename):
    fin = open(filename)
    cases = int(fin.readline().strip())
    lawns = []
    for c in range(cases):
        lawns.append(readLineOfInts(fin))
    return lawns

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if first(s) == last(s):
        if len(s) >= 3:
            return is_palindrome(middle(s))
        else:
            return True
    else:
        return False

# from a project euler problem, #4
def problem4(start, finish):
    palis = []
    for i in range(start,finish+1):
        print i, 
        if is_palindrome(str(i)):
            if is_palindrome(str(i**2)):
                palis.append(i**2)
    #palis.sort()
    print ""
    print "palis: %s" % palis
    return len(palis)

def main(lawns):
    # for each height of lawn mower
    # for each row
    # for each column
    # check if we can mow the lawn like the pattern has
    answers = []
    for l in lawns:
        # print l
        # print math.sqrt(l[0]), math.sqrt(l[1])
        # print int(math.ceil(math.sqrt(l[0]))), int(math.sqrt(l[1]))
        # print "------"
        answers.append(problem4(int(math.ceil(math.sqrt(l[0]))), int(math.sqrt(l[1]))))

    return answers

if __name__ == "__main__":
    filename = "c.in"
    filename = "C-small-attempt0.in"
    lawns = importData(filename)
    answers = main(lawns)
    fout = open("%s.out" % filename, 'w')
    for i in range(len(answers)):
        fout.write("Case #%s: %s\n" % (i + 1, answers[i]))
    print answers

