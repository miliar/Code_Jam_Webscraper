import sys

def translate(dict):
    test_case = int(sys.stdin.readline())
    if not 1 <= test_case <= 30:
        print "invalid number test case"
        sys.exit()
    g = ""
    i = 1
    while(test_case > 0):
        line = str(sys.stdin.readline()).replace('\n','')
        #if len(line)+1 > 100: # verify limit
        new_line = replace_line(dict, line)
        g = g + "Case #" + str(i) + ': ' + new_line + '\n'
        i += 1
        test_case -= 1
    return g

def replace_line(dict, line):
    new_line = ""
    for i in line:
        if i in dict:
            letter = dict[i]
        else:
            letter = i
        new_line += letter
    return new_line

def make_dict(in1, out1):
    d = {}
    pos = 0
    d['y'] = 'a'
    d['e'] = 'o'
    d['q'] = 'z'
    d['z'] = 'q'
    for i in in1:
        if i not in d:
            d[i] = out1[pos]
        pos += 1

    return d


if __name__ == "__main__":
    #real_dict = "abcdefghijklmnopqrstuvwxyz"
    in1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    out1 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    new_dict = make_dict(in1, out1)
    g = translate(new_dict)
    sys.stdout.write(g)
    
