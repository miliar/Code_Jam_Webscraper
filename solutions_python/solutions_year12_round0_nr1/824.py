'''
Created on 2012/04/14

@author: teraotsuyoshi
'''

gdict = dict()

engchar = []
for i in range(26):
    engchar.append(chr(ord('a') + i))
engchar.append(' ')

googchar = []
for i in range(26):
    googchar.append(chr(ord('a') + i))
googchar.append(' ')

print engchar, googchar

eng_str = [
           "a zoo",
           "our language is impossible to understand",
            "there are twenty six factorial possibilities",
            "so it is okay if you want to just give up",
            "q"
           ]
goog_str = [
            "y qee",
            "ejp mysljylc kd kxveddknmc re jsicpdrysi",
           "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
           "de kr kd eoya kw aej tysr re ujdr lkgc jv",
           "z"
            ]



if __name__ == '__main__':
    for j in range(len(eng_str)):
        eng = eng_str[j]
        goog = goog_str[j]
        for i in range(len(eng)):
            if gdict.has_key(goog[i]) and gdict[goog[i]] != eng[i]:
                print "error!", goog[i],eng[i]
                continue
            gdict[goog[i]] = eng[i]
            if eng[i] in engchar:         
                engchar.remove(eng[i])
            if goog[i] in googchar: 
                googchar.remove(goog[i])
            
    print "rest: ", engchar, googchar

    lines = open("input.txt").readlines()
    T = int(lines[0])
    
    for i,line in enumerate(lines):
        if i == 0:
            continue
        print "Case #%d: "%i,
        eng = ""
        for c in line.strip():
            eng = eng + gdict[c]
        print eng
        
        
    
