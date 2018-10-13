INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

L, D, N = [int(i) for i in f_in.readline().split()]

def addToken(list, token):
    retVal = []
    for t in token:
        retVal.extend([(l + t) for l in list]);
    return retVal

def splitIntoTokens(case):
    retVal = []
    cursor = 0
    for j in range(L):
        token = ''
        if case[cursor] != '(':
            retVal.append(case[cursor])
        else:
            cursor = cursor + 1
            token = ''
            while (case[cursor] != ')'):
                token += case[cursor]
                cursor = cursor + 1
            retVal.append(token)
        cursor = cursor + 1;
    return retVal

lang = []
for i in range(D):
    lang.append(f_in.readline().strip());

for i in range(N):
    case = f_in.readline().strip()
    
    tokens = splitIntoTokens(case)
    count = 0
    for word in lang:
        success = True
        for j, letter in enumerate(word):
            if not (letter in tokens[j]):
                success = False
                break;
        if success:
            count = count + 1
    f_out.write("Case #" + str(i + 1) + ": " + str(count) + "\n")

f_in.close()
f_out.close()