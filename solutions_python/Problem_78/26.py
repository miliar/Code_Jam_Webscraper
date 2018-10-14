# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

def problem(N, Pd, Pg):
    if (Pg == 100 and Pd < 100) or (Pg == 0 and Pd > 0):
        return "Broken"
    if N >= 100:
        return "Possible"
    while N > 0:
        if (N * Pd) % 100 == 0:
            print N
            return "Possible"
        N -= 1
    return "Broken"

#----------v
for n in range(int(input.readline())):
#----------^
    N, Pd, Pg = map(int, input.readline().split())
    result = problem(N, Pd, Pg)
#----------v
    print("Case #"+str(n+1)+": "+str(result))
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+str(result)+"\n")
if len(sys.argv) == 3:
    output.close()
#----------^










