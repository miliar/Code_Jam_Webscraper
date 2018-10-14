import sys

def extract(infile):
    answer = int(infile.readline())
    table = []
    for _ in range(4):
        line = infile.readline()
        row = map(int,line.split())
        table.append(row)

    return (answer,table)


def main():
    with open(sys.argv[1]) as infile:
        ntests = int(infile.readline())
        for i in range(1,ntests+1):
            answer1,table1 = extract(infile)
            answer2,table2 = extract(infile)
            set1 = set(table1[answer1 - 1])
            set2 = set(table2[answer2 - 1])

            result = len(set1 & set2)
            if result == 0:
                print "Case #{}: Volunteer cheated!".format(i)
            elif result == 1:
                print "Case #{}: {}".format(i,(set1 & set2).pop())
            else:
                print "Case #{}: Bad magician!".format(i)
            
main()
