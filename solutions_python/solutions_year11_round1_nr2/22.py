import string
import collections

n_cases = input()

for case in xrange(1, n_cases + 1):
    n, m = map(int, raw_input().split())

    d = [raw_input().strip() for _ in xrange(n)]
    l = [raw_input().strip() for _ in xrange(m)]
    dset = set(d)
    ds = dict((letter, set(word for word in d if letter in word)) for letter in string.lowercase)
    
    dsp = dict((letter, dict((word, ''.join(c if c == letter else '_' for c in word)) for word in d if letter in word))
               for letter in string.lowercase)
    dsps = collections.defaultdict(set)

    for letter, di in dsp.iteritems():
        for word, reduc in di.iteritems():
            dsps[reduc].add(word)

    best = []

    for strat in l:
        best_word = ''
        best_score = -1

        for wordn, word in enumerate(d):
            score = 0
            poss = set(w for w in d if len(w) == len(word))
            #print word
            for letter in strat:
                if len(poss) == 1:
                    break
                dsl = ds[letter]
                if not poss.intersection(dsl):
                    #print '',
                    continue

                if letter in word:
                    poss.intersection_update(dsl)
                    poss.intersection_update(dsps[dsp[letter][word]])
                else:
                    score += 1
                    poss.difference_update(dsl)

                #print letter, score, poss

            if score > best_score:
                best_score, best_word = score, word

        best.append(best_word)
            
    print "Case #%d:" % case, " ".join(best)
