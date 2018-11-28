#!/usr/bin/python

# use this file like this:
# ./a.py < ../../Downloads/a.in > a.out

def debug(*arg):
    if DEBUG:
        for x in arg:
            print x,
            print ":",
        print

DEBUG = False

def solver(inp):


    def is_in(word, letters):
        for c in letters:
            if word.count(c) < letters.count(c):
                return False
        return True

    def remove(word, letters):
        #print word, letters
        for c in letters:
            _w = ''
            hit = False
            for _c in word:

                if _c == c and not hit:
                    hit = True
                else:
                    _w = _w + _c
                    #print _w
            word = _w
        return word

    def nums_in(word):
        nums = []
        for lets in l2n.keys():
            if is_in(word, lets):
                nums.append(l2n[lets])
        return nums


    word = inp
    n2l = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"} 
    l2n = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
    ones = {'G': 'EIGHT', 'U':'FOUR', 'W':'TWO', 'X':'SIX', 'Z':'ZERO'}
    nums = []

    hit = True
    c = 0
    while hit and c < 50:
        hit = False
        for unique in ones.keys():
            if unique in word:
                hit = True
                nums.append(l2n[ones[unique]])
                word = remove(word, ones[unique])
                #print word, nums
                c+= 1

    if word:
        st = [(word, nums[:], n) for n in nums_in(word)]
        while word:
            word, nums, n = st.pop()
            #print word, n
            word = remove(word, n2l[n])
            nums.append(n)
            st.extend([(word, nums[:], n) for n in nums_in(word)])






    c=0
    while word and c < 50:
        for lets in l2n.keys():
            if is_in(word, lets):
                nums.append(l2n[lets])
                word=remove(word, lets)
                #print word, nums
                c+= 1
    nums.sort()
    out = ''.join([str(x) for x in nums])

    return [out]
    

cases = int(raw_input())
for case in range(1, cases+1):
    inp = raw_input() #need to add recasting from strings

    print 'Case #{}:'.format(case), ' '.join([str(x) for x in solver(inp)])
 

