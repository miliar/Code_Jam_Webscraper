def tokenize(aString):
    tokens = []
    i = 0
    while i < len(aString):
        token = ""
        if aString[i] == '(':
            while True:
                i = i + 1
                if aString[i] == ")":
                    break
                token = token + aString[i]
        else:
             token = aString[i] 
        tokens.append(token)
        i = i + 1
    return tokens

def check(lexi, tokens):
    for i in range(len(lexi)):
        if len(lexi) != len(tokens):
            return False        
        if len(tokens[i]) > 1:
            if lexi[i] not in tokens[i]:
                return False
        else:
            if lexi[i] != tokens[i]:
                return False
    return True

a = open("input.txt", 'r')
b = open("output.txt", 'w')
L, D, N = a.readline().split(" ")
lexis = []
for i in range(int(D)):
    lexis.append(a.readline())
for i in range(int(N)):
    count = 0
    item = a.readline()
    for j in lexis:
        if check(j, tokenize(item)):
            count = count + 1
    b.write('Case #%s: %s\n' % (i+1, count))

b.close()
a.close()
