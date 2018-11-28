from sys import stdin

def compare_words(word_red_1, word_cnt_1, word_red_2, word_cnt_2):
    if word_red_1 <> word_red_2:
        return -1
    else:
        i = 0
        changes = 0
        while word_cnt_1[i] <> 0:
            changes += abs(word_cnt_1[i] - word_cnt_2[i])
            i += 1
        return changes

def process_word(word):

    word_red = ['']*100
    word_cnt = [0]*100

    prev_ix = 0
    word_red[0] = word[0]
    word_cnt[0] = 1

    for i in xrange(1,len(word)):
        if word[i] <> word_red[prev_ix]:
            prev_ix += 1
            word_red[prev_ix] = word[i]
        word_cnt[prev_ix] += 1 

    return [word_red, word_cnt]

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
 
    nw = int(stdin.readline().strip())
    #print nw

    chars = []
    charnum = []

    line1 = stdin.readline().strip()
    word_red_1, word_cnt_1 = process_word( line1 )
    #print line1
    #print word_red_1
    #print word_cnt_1

    line2 = stdin.readline().strip()
    word_red_2, word_cnt_2 = process_word( line2 )
    #print line2
    #print word_red_2
    #print word_cnt_2

    changes = compare_words( word_red_1, word_cnt_1, word_red_2, word_cnt_2)
    if changes <> -1:
        print "Case #" + str(case_index) + ": " + str(changes)
    else:
        print "Case #" + str(case_index) + ": Fegla Won"

    #for i in xrange(nw):
