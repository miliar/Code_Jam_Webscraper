from sys import argv
googlese = {
    ' ' : ' ',
    '\n' : '\n',
    'a' : 'y',
    'c' : 'e',
    'b' : 'h',
    'e' : 'o',
    'd' : 's',
    'g' : 'v',
    'f' : 'c',
    'i' : 'd',
    'h' : 'x',
    'k' : 'i',
    'j' : 'u',
    'm' : 'l',
    'l' : 'g',
    'o' : 'k',
    'n' : 'b',
    'q' : 'z',
    'p' : 'r',
    's' : 'n',
    'r' : 't',
    'u' : 'j',
    't' : 'w',
    'w' : 'f',
    'v' : 'p',
    'y' : 'a',
    'x' : 'm',
    'z' : 'q'
    }
def solve():
    infile = open(argv[1], 'r')
    outfile = open("outfile.txt", 'w')
    for caseNum in range(1,int(infile.readline())+1):
        outfile.write( "Case #" + str(caseNum) + ": " + 
                       reduce(lambda x,y: x+y,
                              map(lambda z: googlese[z], infile.readline())))
    infile.close()
    outfile.close()

if __name__ == '__main__':
    solve()
