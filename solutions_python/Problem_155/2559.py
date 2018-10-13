__author__ = 'teliov'
import sys


def find_min_invitees(num_peeps, shy_stat):
    invitees = 0
    shy_ok = 0
    count = 0
    for idx in range(int(num_peeps)+1):
        temp = int(shy_stat[count])
        count += 1
        shy_ok += temp
        if shy_ok < count:
            invitees += count - shy_ok
            shy_ok = count
    return invitees


def input_processor(filename):
    filein = open(filename, 'r')
    fileout = open('prob1.txt', 'w')
    num_cases = int(filein.readline())
    print num_cases
    case = 0
    for i in range(num_cases):
        line = filein.readline()
        max_shy = line.split(' ')[0]
        shy_stat = line.split(' ')[1]
        res = find_min_invitees(max_shy, shy_stat)
        case += 1
        writeout = "Case #%d: %s\n" % (case, res)
        fileout.writelines(writeout)

    fileout.close()
    filein.close()

if __name__ == "__main__":
    directory = sys.argv[1]
    print (directory)
    input_processor(directory)