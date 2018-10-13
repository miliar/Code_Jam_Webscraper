def find(s):
    '''
        Input : string s
    '''

    a,b = map(int,s.split())        # print range to variable

    count = 0                       # counter
    for i in range(a,b+1):          # check palindrom
        if i == int(str(i)[::-1]):
            if is_sqrt(i):
                square = int(i**0.5)
                if square == int(str(square)[::-1]):
                        count += 1
    
    return count


def is_sqrt(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1
        if ans*ans != x:  # this if statement was nested inside the while
            return False
        else:
            return True
    else:
        return False


infile = open('C-small-attempt0.in','r') # open input file
output_file = open("output.txt", "w") # open output file

t = int(infile.readline())  # read number of test case

testcase = 1

for line in infile: # start from the second line
    output_file.write("Case #" + str(testcase) + ": " + str(find(line))+"\n")
    testcase+=1

infile.close() # close input file
output_file.close() # close output file
