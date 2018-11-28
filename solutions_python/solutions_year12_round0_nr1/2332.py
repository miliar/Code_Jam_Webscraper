fin = open("A-small-attempt0.in")
fout = open("A-small.out", "w")

fin.readline()

lines = fin.readlines()

mapping = {
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q',
    ' ' : ' ',
    '\n': ''
    }

for j, line in enumerate(lines):
    message = ''.join([mapping[k] for k in line])
    print(message)
    fout.write('Case #' + str(j+1)+ ': ' + message + '\n')

fout.close()    
