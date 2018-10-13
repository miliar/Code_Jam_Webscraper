'''
Created on 12-apr.-2014

@author: Joachim
'''

f =  open("A-small.txt", "r")
out = open("A-small_out.txt", "w")

total_cases = int(f.readline())

for i in xrange(1, total_cases+1):
    row_nr = int(f.readline())
    first_row = []
    for j in xrange(4):
        line = f.readline()
        if (j == row_nr-1):
            first_row = [int(x) for x in line.split(" ")]
    
    row_nr = int(f.readline())
    second_row = []
    for j in xrange(4):
        line = f.readline()
        if (j == row_nr-1):
            second_row = [int(x) for x in line.split(" ")]
            
    intersect = list(set(first_row).intersection(second_row))
    if len(intersect) == 0:
        out.write("Case #%d: Volunteer cheated!\n" % i)
    elif len(intersect) == 1:
        out.write("Case #%d: %d\n" % (i, intersect[0]))
    else:
        out.write("Case #%d: Bad magician!\n" % i)

f.close()
out.close()