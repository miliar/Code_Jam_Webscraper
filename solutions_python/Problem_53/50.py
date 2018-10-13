from sys import argv

def process_file(fin, fout):
    numLines = int(fin.readline())
    for i in range(numLines):
        n, k = map(int, fin.readline().split(' '))
        result = ((k + 1) % (2 ** n) == 0) and "ON" or "OFF"
        fout.write("Case #%s: %s\n" % (i + 1, result))

process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))