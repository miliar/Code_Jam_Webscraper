'''
Created on 14.04.2012

@author: stade
'''


def decrypt():
    f = open("/Users/stade/Downloads/A-small-attempt1.in", "r")
    f.next() # skip firt line
    w = open("/Users/stade/Downloads/output.txt", "w")
    cnt = 1
    for line in f:
        sol = translate(line.strip())
        print "Case #%d: %s" %(cnt, sol)
        w.write("Case #%d: %s\n" %(cnt, sol))
        cnt += 1
    w.close()

def generate_charmap():
    
    in_str0 = "aoz"
    in_str1 = "our language is impossible to understand"
    in_str2 = "there are twenty six factorial possibilities"
    in_str3 = "so it is okay if you want to just give up"
    out_str0 = "yeq"
    out_str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    out_str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    out_str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    
    charmap = dict()
    for char_in, char_out in zip(in_str0, out_str0):
        charmap[char_in] = char_out
    for char_in, char_out in zip(in_str1, out_str1):
        charmap[char_in] = char_out
    for char_in, char_out in zip(in_str2, out_str2):
        charmap[char_in] = char_out
    for char_in, char_out in zip(in_str3, out_str3):
        charmap[char_in] = char_out

    #manual mapping "z"
    charmap["z"] = "q"
    return charmap


def translate(txt):
    charmap = generate_charmap()
    rev_charmap = dict((v,k) for k, v in charmap.iteritems())
    rev_charmap["z"] = "q"
    translated_txt = []
    for i in range(len(txt)):
        translated_txt.append(rev_charmap[txt[i]])
    print "".join(translated_txt)
    return "".join(translated_txt)

if __name__ == '__main__':
   decrypt()