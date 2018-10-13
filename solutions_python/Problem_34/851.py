'''
Alien Language

Problem

After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.
'''
import re

def conv_pattern(r):
    all_s = re.split("\(\w+\)",r)
    all_p = re.findall(r"(\w+)",r)
    for p in all_p:
        if p in all_s: yield p
        else:
            yield "(%s)" % "|".join(p)

if __name__ == '__main__':
    data = open("A-small-attempt7.in").read()
    data = data.split("\n")
    l,d,n = data[0].split(" ")
    l,d,n = int(l),int(d),int(n)
    d_data = data[1:d+1]
    n_data = data[d+1:]
    
    results = []
    for p in n_data:
        i = 0
        if p=="":continue
        pattern = "".join(list(conv_pattern(p)))
        for v in d_data:
            if re.match(pattern,v):
                i+=1
        results.append(i)
    
    f = open("A-small-attempt7.out","w")
    for i,r in enumerate(results):
        f.write("Case #%s: %s\n" % (i+1,r))
    f.close()
    
