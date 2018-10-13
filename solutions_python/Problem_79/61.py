from pprint import pprint

# by: Jeremy Holman, jeremy.holman@gmail.com
# for: Google Code Jam 2011, Round 1A
# problem B: The Killer Word

T = int(raw_input().strip())        # grabs an integer from stdin

def calc_score_help(words, word, alpha):
    lenwords = filter(lambda x: len(x)==len(word), words)
    ans = calc_score(lenwords,word,alpha)
    return ans

def make_letter_mask(letter, word):
    return ''.join(a if a is letter else ' ' for a in word)

def calc_score(words, word, alpha):
    if len(words) == 1 or len(alpha)==0:
        #print "he knows the answer at this point"
        return 0
    letter = alpha[0]
    words_with_letter = [w for w in words if letter in w]
    if any(words_with_letter):
        #print "he guesses %s" % letter
        if letter in word:
            #print "fine, give it to him"
            words_aligned = filter(lambda x: make_letter_mask(letter,x) == make_letter_mask(letter,word), words)
            return calc_score(words_aligned, word, alpha[1:])
        else:
            #print "haha, sucker, take a hit!"
            words_no_letter = [w for w in words if letter not in w]
            return 1 + calc_score(words_no_letter, word, alpha[1:])
    else:
        #print letter +" is not available, so is not used.  skip to next letter."
        return calc_score(words,word,alpha[1:])
    raise Exception("this should not be possible")


for case in range(1,T+1):
    N,M = map(int,raw_input().strip().split(' '))


    words = []

    for i in range(N):
        words.append(raw_input().strip())

    answers = []
    for i in range(M):
        alpha = raw_input().strip()
        costs = map(lambda x:calc_score_help(words, x, alpha), words) # raw costs
        max_cost = max(costs)
        cost_tuples = zip(words,costs)
        best_tuples = filter(lambda (x,y): y == max_cost, cost_tuples)
        best_tuple = best_tuples[0]
        best_word = best_tuple[0]
        answers.append(best_word)

    print "Case #%d: %s" % (case, ' '.join(answers))
