def solve(N):
    while (not (list(str(N)) == sorted(list(str(N))))):
        N -= 1
    return N
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsRead = readFile("B-small-attempt0.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    N = int(c)
    res = solve(N)
    contentsToWrite += "Case #%d: " % count
    contentsToWrite += "%d" % res if type(res) == int else res 
    contentsToWrite += "\n"
    count+=1

writeFile("out.txt",contentsToWrite)
