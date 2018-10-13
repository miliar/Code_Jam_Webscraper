from sys import stderr, stdout

def matches(word, tokens):
    for i in range(len(word)):
        if word[i] not in tokens[i]:
            return 0
    return 1

def solve_case(pattern, alien_words, L):

    tokens = [0] * L
    # Split the pattern
    token_index = 0
    i = 0
    while i < len(pattern):
        if pattern[i] == '(':
            # read the next token, until )
            token_end = pattern.find(")", i)
            tokens[token_index] = pattern[i+1:token_end]
            token_index += 1
            i = token_end + 1
        else:
            # normal character
            tokens[token_index] = pattern[i]
            token_index += 1
            i += 1

    #print >> stderr, pattern
    #print >> stderr, tokens

    # Check which alien words match the pattern
    num_words = 0

    for word in alien_words:
        num_words += matches(word, tokens)

    return num_words


if __name__ == '__main__':

    # Read the input
    (L, D, N) = raw_input('').split(' ')
    L = int(L)
    D = int(D)
    N = int(N)

    # Read alien words
    alien_words = set()
    for word_ind in range(D):
        word = raw_input('')
        alien_words.add(word)

    #print >> stderr, alien_words
        
        # Read patterns
    for pat_ind in range(N):
        pat = raw_input('')

        print >> stderr, 'Solving case %d' % (pat_ind + 1)
        sol = solve_case(pat, alien_words, L)

        print "Case #%d: %d" % (pat_ind + 1, sol)


