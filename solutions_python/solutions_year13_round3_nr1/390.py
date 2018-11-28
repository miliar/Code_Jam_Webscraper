
f = open('1.ex', 'r')
fo = open('1.out', 'w+')

T = int(f.readline())

vowels = ['a', 'e', 'i', 'o', 'u']

def substring_found(n, L, substring_begin_index, begin_index_of_last_substring=-1):
    substring_end_index = substring_begin_index + n
    after_substrings = L - substring_end_index
    before_substrings = substring_begin_index - begin_index_of_last_substring
    substrings = (1+after_substrings) * before_substrings
    return substrings

for case in xrange(T):
    tokens = f.readline().split()
    
    name = tokens[0]
    n = int(tokens[1])
    L = len(name)
    
    substrings = 0
    begin_index_of_last_substring = -1
    
    # Find first substring
    for letter_index in xrange(L):
        letter = name[letter_index]
        consonants = 0
        while not letter in vowels:
            consonants += 1
            if consonants >= n:
                substrings += substring_found(n, L, letter_index, begin_index_of_last_substring)
                begin_index_of_last_substring = letter_index
                break
            try:
                letter = name[letter_index+consonants]
            except IndexError:
                break
    
    fo.write('Case #' + str(case+1) + ': ' + str(substrings) + '\n')