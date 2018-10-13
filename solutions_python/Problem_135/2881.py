from sys import stdin, stdout


def doMagic():
    row1 = getRow()
    row2 = getRow()

    common = row1.intersection(row2)
    
    l = len(common)
    if l == 1:
        stdout.write(list(common)[0])
        return
    if l == 0:
        stdout.write("Volunteer cheated!")
        return
    stdout.write("Bad magician!")
    return
    

def getRow():
    row_num = int(stdin.readline().strip())
    for i in range(row_num):
        row = stdin.readline()

    for i in range(4 - row_num):
        stdin.readline()

    row = set(row.strip().split(' '))
    return row


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())
    for i in range(num_cases):
        stdout.write("Case #" + str(i + 1) + ": ")
        doMagic()
        stdout.write("\n")
