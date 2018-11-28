import itertools
from codejam import CodeJam

def uniq(iterable):
   r = []
   for i in iterable:
       if r == [] or i != r[-1]: r.append(i)
   return r

def get_words_count(words, search_engines):
    ret_word_dict = []
    total = len(words)
    for i in xrange(total):
        candidate = ()
 
        # make dict
        candidate = (0, None)

        for se in search_engines:
            if words[i:].count(se) == 0:
                candidate = (0, se)
                break
        else:
            for word in words[i:]:
                actual = words[i:].index(word)
                if actual >= candidate[0] and actual != 0:
                    candidate = (actual, word)

        ret_word_dict.append(candidate)

    return ret_word_dict

cj = CodeJam(debug=False)
cases = cj.get_int()

for case in xrange(cases):
    search_engines = cj.get_lines(cj.get_int())
    words = cj.get_lines(cj.get_int())

    switch = 0
    if words:
        words_best = get_words_count(words, search_engines)

        actual = ''
        for i in xrange(len(words)):
            if i == 0 or actual == words[i]:
                actual = words_best[i][1]
                if i != 0: switch += 1
    
    print switch
    cj.write_case(switch)
