
import sys

if __name__ == '__main__':

    testCasesCount = raw_input()
    for i in range(0, int(testCasesCount)):
        firstAns = raw_input()
        for j in range(1, 5):
            inline = raw_input()
            if j == int(firstAns):
                line_one = map(int, inline.split())
        secAns = raw_input()
        for j in range(1, 5):
            inline = raw_input()
            if j == int(secAns):
                line_two = map(int, inline.split())

        common = set(line_one) & set(line_two)
        lenCommon = len(common)
        sys.stdout.write("Case #" + str(i + 1) + ": ")
        if lenCommon > 1:
            print "Bad magician!"
        elif lenCommon == 0:
            print "Volunteer cheated!"
        else:
            print list(common)[0]
