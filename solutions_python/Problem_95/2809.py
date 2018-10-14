d = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'x': 'm',
    'z': 'q',
    'w': 'f',
    'y': 'a',
    'k': 'i'
}

fin = open('codejam_input', 'r')
fout = open('codejam_output', 'w')

t = int(fin.readline())
if t >= 1 and t <= 30:
    for i in range(1, t+1):
        g = fin.readline().rstrip('\n');
        g_len = len(g)
        if (g_len <= 100):
            output = 'Case #'+str(i)+': '
            for j in range(g_len):
                if g[j] != ' ':
                    output += d[g[j]]
                else:
                    output += ' '
            fout.write(output+'\n')
        
