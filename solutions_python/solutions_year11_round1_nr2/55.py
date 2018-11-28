#!pypy
#pypy 1.5 JIT (like python2.7) on OS X
import sys
import collections
deq = collections.deque


def solve(words, lists):
    words_by_letter = collections.defaultdict(set)
    words_by_indexed_letters = collections.defaultdict(set)
    words_by_letter_indexes = collections.defaultdict(set)
    words_by_length = collections.defaultdict(set)
    
    index_by_word = dict()
    letter_indexes_by_word = dict()
    
    for i, word in enumerate(words):
        index_by_word[word] = i
        words_by_length[len(word)].add(word)
        
        letter_indexes_by_word[word] = collections.defaultdict(set)
        
        for j, letter in enumerate(word):
            words_by_letter[letter].add(word)
            words_by_indexed_letters[j, letter].add(word)
            letter_indexes_by_word[word][letter].add(j)
        
        for letter, indexes in letter_indexes_by_word[word].items():
            frozen_indexes = frozenset(indexes)
            letter_indexes_by_word[word][letter] = frozen_indexes
            letter_indexes_by_word[word].default_factory = frozenset
            words_by_letter_indexes[letter, frozen_indexes].add(word)
    
    def attempt(word, letters):
        # return the number of points lost given word and letters
        
        lost = 0
        possibilities = words_by_length[len(word)].copy()
        
        for letter in letters:
            if len(possibilities) <= 1:
                break
            
            possibilities_with_letter = possibilities & words_by_letter[letter]
            
            if possibilities_with_letter: # then we guess it
                result_indexes = letter_indexes_by_word[word][letter]
                
                if words_by_letter_indexes[letter, result_indexes] == possibilities:
                    continue
                
                if letter in word:
                    possibilities &= words_by_letter_indexes[letter, result_indexes]
                else:
                    possibilities -= possibilities_with_letter
                    lost += 1
        
        assert len(possibilities) == 1
        
        return lost
    
    results = []
    
    for letters in lists:
        max_lost = -1
        max_word = "ERROR"
        
        for word in words:
            word_max = attempt(word, letters)
            
            if word_max > max_lost:
                max_lost = word_max
                max_word = word
        
        results.append(max_word)
    
    return " ".join(results)

lines = deq(line.strip() for line in sys.stdin)
total_cases = int(lines.popleft())

for n in range(1, total_cases + 1):
    n_words, n_lists = map(int, lines.popleft().split())
    
    words = []
    for _ in range(n_words):
        words.append(lines.popleft())
    
    lists = []
    for _ in range(n_lists):
        lists.append(lines.popleft())
    
    result = solve(words, lists)
    
    print "Case #%s: %s" % (n, result)

