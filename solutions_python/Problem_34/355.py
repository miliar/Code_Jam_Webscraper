import sys

letters = 'abcdefghijklmnopqrstuvwxyz'

def test_cases(FILE):
    f = open(FILE)
    total = f.readline()
    total = total.split()
    L = int(total[0])
    D = int(total[1])
    N = int(total[2])
    words = []
    patterns = []
    for i in range(0,D):
        word = f.readline()
        words.append(word)
    for i in range(0,N):
        pattern = f.readline()
        patterns.append(pattern)
    return (L,D,N,words,patterns)

def create_pattern(pattern):
    r = []
    inside = False
    for c in pattern:
        if c == '(':
            inside = True
            t = []
        elif c == ')':
            inside = False
            r.append(t)
        else:
            if inside:
                t.append(c)
            else:
                r.append([c])
    return r


def chr_index(char):
    return letters.find(char)

def solve(trie, pattern, L):
    level = 0
    solutions = 0
    pattern = create_pattern(pattern) # disecar el pattern
    where = [-1 for i in range(0,L)] # donde estoy en cada parte del pattern
    stack = [trie]
    
    while level >= 0: 
        where[level] += 1 # avanzo en el level
        pos = where[level] # pos me dice dodne estoy en la parte actual del pattern (la del level)
        if pos >= len(pattern[level]): # me pase, backtack
            where[level] = -1 # reseteo donde estaba
            level -= 1 # me bajo un nivel
            stack.pop()
        else:
            letter_index = chr_index(pattern[level][pos]) #indice la letra que estoy analizando (letra del level y pos)
            if level == (L-1): # si estoy en el ultimo nivel chequeo si es una solucion
                if stack[-1][letter_index]:
                    solutions += 1
            else: # si no estoy en el ultimo nivel, avanzo de level (solo si hay algo en el trie)
                next = stack[-1][letter_index]
                if next:
                    level += 1
                    stack.append(next)
    return solutions

def init_trie(L, words):
    def empty():
        return [None for i in range(0,len(letters))]
    
    trie = empty()
    
    for word in words:
        i = 0
        t = trie
        for c in word:
            index = chr_index(c)
            if i == (L-1):
                t[index] = True
            else:
                if t[index] is None:
                    t[index] = empty()
                t = t[index]
                i += 1
            
    return trie
    
#def init_trie(L):
#    trie = []
#    for i in range(0, len(letters)):
#        if L == 1:
#            trie.append(False)
#        else:
#            trie.append(init_trie(L-1))
#    return trie

def add_words(trie, words, L):
    for word in words:
        t = trie
        for i in range(0,L):
            pos = chr_index(word[i])
            if i < (L-1):
                t = t[pos]
            else:
                t[pos] = True
    
def do_A(FILENAME):
    (L,D,N,words,patterns) = test_cases(FILENAME)
    words = map(lambda x: x[0:-1], words)
    patterns = map(lambda x: x[0:-1], patterns)
    trie = init_trie(L, words)
    #add_words(trie,words, L)
    solutions = []
    for pattern in patterns:
        solution = solve(trie, pattern, L)
        solutions.append(solution)
    return solutions
 
def output(solutions):
    f = open('C:\\output_A.txt', 'w')
    i = 1
    for solution in solutions:
        f.write("Case #%s: %s\r\n" % (i,solution))
        i += 1
    f.close()
    
if __name__ == '__main__':
    solutions = do_A(sys.argv[1])
    output(solutions)