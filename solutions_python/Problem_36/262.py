INPUT = 'C-small.in'
OUTPUT = 'C-small.out'
STRING = 'welcome to code jam'

def findRecursively(index, searchedString):
    found = 0
    for i in range(len(searchedString)):
        if len(STRING[index:]) > len(searchedString[i:]):
            break
        if searchedString[i] == STRING[index] and index == len(STRING)-1:
            found += 1
        elif searchedString[i] == STRING[index]:
            found += findRecursively(index+1, searchedString[i+1:])
    return found


if __name__ == '__main__':

    infile = open(INPUT)
    output = open(OUTPUT, 'w')
    N = int(infile.readline().strip())

    for case in range(N):
        string = infile.readline().strip()
        f = findRecursively(0, string)
        f = str(f)
        if len(f) > 4:
            f = f[-4:]
        output.write("Case #%d: %s\n" % (case+1, f.zfill(4)))
    infile.close()
    output.close()
