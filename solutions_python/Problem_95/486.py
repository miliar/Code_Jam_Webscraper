import sys, os

def solve(filename, dict):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                print "Case #%s: %s" % (case, translate(line.strip(), dict))
                case += 1

def translate(string, dict):
    return "".join([dict[c] for c in string])
                
def make_dict():
    ret = {"y": "a",
           "e": "o",
           "q": "z",
           "z": "q"}
                    
    input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    output = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    for i, char in enumerate(input):
        if char in ret:
            assert ret[char] == output[i], "expected mapping %s -> %s but was %s" % (char, ret[char], output[i])
        else:
            ret[char] = output[i]
    return ret    

if __name__ == "__main__":
    the_dict = make_dict()
    solve("A-small-attempt1.in", the_dict)