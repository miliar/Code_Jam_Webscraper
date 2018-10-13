import sys
from fnmatch import filter


def read_case(infile):
    N, M = map(int, infile.readline().split())
    dictionary = [infile.readline().strip() for i in range(N)]
    lists = [infile.readline().strip() for i in range(M)]
    return (dictionary, lists)


def letters_in(words):
    letters = set()
    for word in words:
        for c in word:
            letters.add(c)
    return letters

def fill_in(word, board, c):
    for i in range(len(board)):
        if word[i] == c:
            board[i] = c
    return board

def make_pattern(board, in_word):
    p = []
    for c in board:
        if c == None:
            p.append('[!%s]' % in_word)
        else:
            p.append(c)
    return ''.join(p)

def get_score(dictionary, word, order):
    score = 0
    n = len(word)
    new_dictionary = [w for w in dictionary if len(w) == n]
    dictionary = new_dictionary
    letters = letters_in(dictionary)
    board = [None] * n
    in_word = ''
    for c in order:
        if c in letters:
            if c in word:
                in_word += c
                fill_in(word, board, c)
                p = make_pattern(board, in_word)
                new_dictionary = filter(dictionary, p)
                dictionary = new_dictionary
                letters = letters_in(dictionary)
            else:
                dictionary = [w for w in dictionary if c not in w]
                letters = letters_in(dictionary)
                score -= 1
    return score
        
    

def solve_order(dictionary, order):
    min_score = 1
    result = ''
    for word in dictionary:
        score = get_score(dictionary, word, order)
        if score < min_score:
            result = word
            min_score = score
    return result
    
def solve_case(dictionary, lists):
    words = [solve_order(dictionary, order) for order in lists] 
    return ' '.join(words)


if __name__ == '__main__':
    infile = sys.stdin
    T = int(infile.readline())      
    for i in range(T):
        (dictionary, lists) = read_case(infile)
        result = solve_case(dictionary, lists)
        print "Case #%d: %s" % (i + 1, result)
    
