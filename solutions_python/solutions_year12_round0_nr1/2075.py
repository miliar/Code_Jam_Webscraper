import pprint
import string
import fileinput

def get_trans(clear,cipher):
    trans = {}
    for (s,d) in zip(clear,cipher):
        if d in trans and trans[d] != s:
            print "conflicting input:",d,s,trans[d]
        trans[d] = s
    return trans

def complete_trans(partial_trans):
    srcLetter = None
    dstLetter = None
    existingSrcLetters = set(partial_trans.keys())
    existingDstLetters = set(partial_trans.values())
    for letter in string.ascii_lowercase:
        if letter not in existingSrcLetters:
            assert srcLetter == None
            srcLetter = letter
        if letter not in existingDstLetters:
            assert dstLetter == None
            dstLetter = letter
    assert srcLetter != None and dstLetter != None
    partial_trans[srcLetter] = dstLetter
    return partial_trans
            

#This code was used to determine the missing character in the translation table:
#trans = get_trans("aozour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up","yeqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv")
#trans = complete_trans(trans)
#pprint.pprint(trans)
#print len(trans)

trans = string.maketrans("zyeqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv","qaozour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up")

def main():
    it = fileinput.input()
    numcases = int(it.next())
    for i,l in enumerate(it):
        print "Case #%d: %s" % (i+1,string.translate(l,trans,"\n"))

if __name__ == "__main__":
    main()

