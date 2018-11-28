'''
Created on 2009. 9. 3.

@author: Bang, Hyunsu
'''

def process(data, words_lists):
#    print data
    letter_set = list()
    in_brace = False
    braced = list()
    for letter in data:
        if (letter == '('):
            in_brace = True
            continue
        if (letter == ')'):
            in_brace = False
            letter_set.append(''.join(braced))
            braced = list()
            continue
        if not in_brace:
            letter_set.append(letter)
        else:
#            print letter
            braced.append(letter)
#    print letter_set
    res = 0
    for word in words_lists:
        has_word = True
        for i, char in enumerate(word):
            if not char in letter_set[i]:
                has_word = False
                break
        if has_word:
            res += 1
    return res

def main(input_fn):
    try:
        f = open(input_fn, 'r')
        o = open(input_fn+'.out', 'w')
    except IOError:
        print "Input file %s dos not exists" % (input_fn, )
        return 2
    
    letters, words, cases = f.readline().strip().split()
    words_list = list()
    for ln in range(int(words)):
        words_list.append(f.readline().strip())
    print words_list
    for i in range(int(cases)):
        ret = process(f.readline().strip(), words_list)
        print ret
        o.write('Case #' + str(i+1) + ': ' + str(ret) + '\n')
    
import sys
if __name__ == '__main__':
    main(sys.argv[1])