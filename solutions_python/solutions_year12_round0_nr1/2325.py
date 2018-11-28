import sys

def frequency(string, counts):
    for char in string:
        counts[char] = counts.get(char,0) + 1

def analyze_frequencies(cases):
    counts = {}
    for case in cases:
        frequency(case, counts)
    return counts

def translate(string, tdict):
    result = ""
    for char in string:
        result += tdict[char]
    return result

def rosetta(googleese, english, tdict):
    both = zip(googleese,english)
    for g, e in zip(googleese,english):
        if g in tdict and tdict[g] != e:
            raise Exception(googleese, english, tdict, g,e)
        tdict[g] = e
def startup():
    googleese = """ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv"""
    googleese = [x.strip() for x in googleese.split("\n")]
    english = """our language is impossible to understand
    there are twenty six factorial possibilities
    so it is okay if you want to just give up"""
    english = [x.strip() for x in english.split("\n")]
    tdict = {'y' : 'a', 'e' : 'o', 'q' : 'z'}
    for google, english in zip(googleese, english):
        rosetta(google, english, tdict)
    alphaset = set("abcdefghijklmnopqrstuvwxyz")
    leftover_g = alphaset - set(tdict.keys())
    leftover_e = alphaset - set(tdict.values())
    if len(leftover_g) != 1 or len(leftover_e) !=1:
        raise Exception("Incomplete rosetta")
    tdict[leftover_g.pop()] = leftover_e.pop()
    return tdict
 
def translate_lines(lines, tdict):
    for i, line in enumerate(lines):
        line = line.strip()
        print "Case #%s: %s" % (i+1, translate(line, tdict))

if __name__ == '__main__':
    tdict = startup()
    translate_lines(open(sys.argv[1]).readlines()[1:], tdict)

