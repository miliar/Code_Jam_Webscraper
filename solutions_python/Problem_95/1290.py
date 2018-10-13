import pprint
import codecs
import copy

def toEnglish(G):
    print G
    answer = ''
    for g in G:
        if g in dict:
            print g + ' ' + dict[g]
            answer = answer + dict[g]
    print answer
    return answer

dict = {
        'y': 'a',
        'n': 'b',
        'f': 'c',
        'i': 'd',
        'c': 'e',
        'w': 'f',
        'l': 'g',
        'b': 'h',
        'k': 'i',
        'u': 'j',
        'o': 'k',
        'm': 'l',
        'x': 'm',
        's': 'n',
        'e': 'o',
        'v': 'p',
        'z': 'q',
        'p': 'r',
        'd': 's',
        'r': 't',
        'j': 'u',
        'g': 'v',
        't': 'w',
        'h': 'x',
        'a': 'y',
        'q': 'z',
        ' ': ' '
        }
file = codecs.open("googlerese.small.in", encoding="utf-8", mode="r")
outfile = codecs.open("googlerese.small.out", encoding="utf-8", mode="w")
totalCases = int(file.readline())
for case in range(totalCases):
    G = file.readline()
    answer = toEnglish(G)
    print "Case #" + str(case+1) + ": " + answer
    outfile.write("Case #" + str(case+1) + ': ' + answer + '\n')
