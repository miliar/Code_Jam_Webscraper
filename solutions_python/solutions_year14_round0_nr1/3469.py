import sys
import struct, string, math
from collections import Counter


def main(argv = None):
    if argv is None:
        argv = sys.argv

    if (len(argv) != 3):
        print(len(argv))
        print("Wrong number of arguments")
        return
    f = open (argv[1], 'r')
    lines = f.readlines()
    CaseNum = int(lines[0])
    origin_stdout = sys.stdout
    w = open (argv[2], 'w')
    sys.stdout = w
    for i in range(CaseNum):
        row1 = int(lines[10*i+1])
        inline1 = lines[10*i+1+row1].strip().split()
        row2 = int(lines[10*i+6])
        inline2 = lines[10*i+6+row2].strip().split()
        common = list((Counter(inline1) & Counter(inline2)).elements())
        
        if len(common)==0:
            print("Case #%s: Volunteer cheated!" %(i+1))
        if len(common)==1:
            print("Case #%s:" %(i+1), common[0])
        if len(common)>=2:
            print("Case #%s: Bad magician!" %(i+1))
    sys.stdout = origin_stdout
    w.close()
    f.close()
    return

if __name__ == '__main__':
    main()
