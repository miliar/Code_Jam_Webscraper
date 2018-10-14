alpha = {}

inputcases = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 
                'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    
outputcases = ['our language is impossible to understand',
                'there are twenty six factorial possibilities',
                'so it is okay if you want to just give up']

def populate_dict(dictionary):
    for i in range(ord('a'), ord('z')+1):
        alpha[chr(i)] = ''

def mapalph(string1, string2):
    c = 0
    
    while c < len(string1):
        if string1[c] != ' ':
            alpha[string1[c]] = string2[c]
        c += 1

def get_letters(inputc, outputc):
    d = 0
    while d < len(inputcases):
        mapalph(inputc[d], outputc[d])
        d += 1

def translate(instring):
    output = ''
    ocases = []
    alpha['z'] = 'q'
    alpha['q'] = 'z'
    alpha[' '] = ' '

    for i in instring:
        for j in i:
            if alpha.get(j) != None:

                output += alpha.get(j)

        ocases.append(output)
        output = ''

    return ocases
    
def main():
    f = open('input.txt', 'r')
    o = open('output.txt', 'w')
    
    ncases = f.readline()
    cases = []
    ocases = []
    for i in range(int(ncases)):
        cases.append(f.readline())
        
    populate_dict(alpha)
    get_letters(inputcases, outputcases)

    ocases = translate(cases)
    for i in range(len(ocases)):
        o.write('Case #' + str(i+1) + ": " + ocases[i] + '\n')

    f.close()
    o.close()
    
    
    
if __name__ == '__main__':
    main()
