from io import StringIO
import sys

sample = u"""3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16"""

# in_f = StringIO(sample)
#in_f = sys.stdin
in_f = open('A-small-attempt1.in')
out_f = open("a1.out",'w')

T =  int(in_f.readline())

for case in range(T):
    answer1 = int(in_f.readline())
    row1 = [in_f.readline() for _ in range(4)][answer1-1].split()
    answer2 = int(in_f.readline())
    row2 = [in_f.readline() for _ in range(4)][answer2-1].split()
    res = list(set(row1).intersection(row2))
    out_f.write("Case #%s: " % (case+1,))
    if len(res) == 0:
        out_f.write("Volunteer cheated!\n")
    elif len(res) == 1:
        out_f.write(res[0]+"\n")
    else:
        out_f.write("Bad magician!"+"\n")








