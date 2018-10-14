f = open('A-small-attempt1.in')
output = open('outtounges.out', 'w')

lettermap = {'z':'q','y':'a', 'e':'o', 'q':'z', 'j':'u', 'm':'l','s':'n', 'l':'g','c':'e', 'k':'i','d':'s','x':'m', 'v':'p','n':'b','r':'t','t':'w','i':'d','p':'r','b':'h','a':'y','h':'x', 'w':'f','f':'c','o':'k','u':'j', 'g':'v',}
cases = int(f.readline())

def solve():
    line = f.readline()
    solvedline = ''
    for letter in line:
        if letter == ' ':
            solvedline += ' '
        elif letter == '\n':
            return solvedline
        else:
            solvedline += lettermap[letter]
    return solvedline

for x in range(cases):
    output.write('Case #' + str(x+1)+': ' + solve() + '\n')
output.close()
    
