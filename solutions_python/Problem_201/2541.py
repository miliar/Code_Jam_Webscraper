# Open the given file 
lines = open("input.txt", "r").readlines()
n = int(lines[0].strip())

# Represent the bathroom sections as (L,a,b), where L is the
# number of free stalls, a is first occupied stall to the left,
# and b is the first occupied stall to the right. I.e. L=b-a..

# Read the data from

# Create a function to split such a tuples in two parts
def make_two(tup):
    a = int(tup[1])
    b = int(tup[2])
    m = (a+b) // 2
    return (-(m-a-1),a,m), (-(b-m-1),m,b)

# Create a function to determine max(LS,RS) and min(LS,RS)
def max_min(n,k):
    sections = [(-n,0,n+1)]
    for i in range(k):
        sections.sort()
        section = sections.pop(0)
        sections.append(make_two(section)[0])
        sections.append(make_two(section)[1])
        #print(sections)
    LS = sections[-2][2] - sections[-2][1] - 1
    RS = sections[-1][2] - sections[-1][1] - 1
    answer1 = max(LS, RS)
    answer2 = min(LS, RS)
    return str(answer1) + " " + str(answer2)
        
# Create a file for the answer and line by line write last tidy number
outfile = open("answer.txt", "w")
for j in range(1,n+1):
    n, k = lines[j].split()
    n, k = int(n), int(k)
    answer = max_min(n,k)
    line = "Case #" + str(j) + ": " + str(answer) + "\n"
    outfile.write(line)
outfile.close()

