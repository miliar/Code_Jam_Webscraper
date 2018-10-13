name = 'A-large.'
vstup = file(name+'in').read()

def check(word):
    wi = pi = -1
    while wi < len(word)-1:
        wi += 1
        pi += 1
        if pattern[pi] == '(':
            end_at = pattern.find(')', pi+1)
            possible = pattern[pi+1:end_at]
            pi = end_at
            if word[wi] in possible: continue
        if word[wi] == pattern[pi]: continue
        return False
    return True
        

lines = vstup.split('\n');
L, D, N = (int(c1) for c1 in lines[0].split(' '))
words = lines[1:D+1]
tests = lines[D+1:D+N+1]
# print L
# print words
# print tests

i = 1
vystup = file(name+'out', 'w')
for pattern in tests:
    vystup.write('Case #'+str(i)+': '+str(len(filter(check, words)))+'\n')
    i+=1
vystup.close()
