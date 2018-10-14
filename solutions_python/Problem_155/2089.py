class gcjInFile(object):
    def __init__(self, infile, linesPerCase = 1):
        self._file = open(infile)
        self._linesPerCase = linesPerCase
        self._len = int(self._line())
    
    def __len__(self):
        return self._len
    
    def _line(self):
        return self._file.readline()
    
    def __iter__(self):
        for caseNum in range(1, len(self)+1):
            case = []
            for caseline in range(1, self._linesPerCase+1):
                line = self._line()
                if not line:
                    raise StopIteration
                entry = []
                start, end = 0, line.find(" ")
                if end == -1: end = len(line)-1
                while (start < end):
                    entry.append(line[start:end])
                    start = end + 1
                    end = line.find(" ", start)
                    if end == -1: end = len(line)-1
                case.append(entry)
            yield tuple(case)

def minFriends(shyness):
    standing = 0
    added = 0
    for i,n in enumerate(shyness):
        if not int(n):
            continue
        if i<=standing:
            standing += int(n)
            continue
        added += i-int(standing)
        standing += i-int(standing) + int(n)
    return str(added)

myGcjInFile = gcjInFile('/tmp/A-large.in', 1)
myGcjOutFile = '/tmp/A-large.out'
with open(myGcjOutFile, "w") as f:
    number = 0
    for case in myGcjInFile:
        number += 1
        shyness = case[0][1]
        
        f.write("Case #" + str(number) + ": " + minFriends(shyness) + "\n")