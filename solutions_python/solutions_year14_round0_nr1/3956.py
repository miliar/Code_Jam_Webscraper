# GCJ Magic Trick

## file io template
input = "magician.in"
output = "magician.out"
def fread(filename):
    with open(filename, "r") as fin:
        for line in fin:
            yield line.strip().split()

def fwrite(line):
    with open(output, 'a') as fout:
        fout.write(line)
        if "\n" not in line:
            fout.write("\n")

read = fread(input).next
## end template

T = int(read()[0])

for testcase in xrange(T):
    firstrownum = int(read()[0]) - 1
    for i in xrange(firstrownum):
        read() # skip lines until row chosen
    candidates = set(map(int, read()))
    for i in xrange(3-firstrownum):
        read() # skip rows after
    secondrownum = int(read()[0]) - 1
    for i in xrange(secondrownum):
        read() # skip lines until row chosen
    candidates &= set(map(int, read()))
    for i in xrange(3-secondrownum):
        read() # skip rows after
    overlap = len(candidates)
    if overlap == 1:
        fwrite("Case #" + str(testcase+1) + ": " + str(candidates.pop()))
    elif overlap == 0:
        fwrite("Case #" + str(testcase+1) + ": Volunteer cheated!")
    else:
        fwrite("Case #" + str(testcase+1) + ": Bad magician!")