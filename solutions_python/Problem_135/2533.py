
def main():
    outfile = open('output.txt', 'w')
    infile = open('input.txt', 'r')

    n = int(infile.readline())
    for i in range(n):
        rownum = int(infile.readline())
        for rows in range(1,5,1):
            row = infile.readline()
            if rows == rownum:
                row1 = row.split()
        rownum = int(infile.readline())
        for rows in range(1,5,1):
            row = infile.readline()
            if rows == rownum:
                row2 = row.split()
    
        common = findCommon(row1, row2)
        if len(common) == 0:
            outfile.write('Case #' + str(i+1) + ': Volunteer cheated!\n')
        elif len(common) == 1:
            outfile.write('Case #' + str(i+1) + ': ' + common[0] + '\n')
        else:
            outfile.write('Case #' + str(i+1) + ': Bad magician!\n')

    infile.closed
    outfile.closed

def findCommon(row1, row2):
    common = []
    for x in row1:
        if x in row2:
            common.append(x)
    return common

if __name__ == "__main__":
    main()
