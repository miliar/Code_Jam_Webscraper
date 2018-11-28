istr = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up" ]
astr = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
##
##lang_dict = dict()
##for (ielem, aelem) in zip(istr, astr):
##    print "---------------------------------------------------"
##    for (i,j) in zip(ielem, aelem):
##        ij = i + j
##        if ij in lang_dict.keys():
##            continue
##        #print i, "\t->\t", j, "\t:\t", ord(i), "\t->\t", ord(j)
##        lang_dict[ij] = 1
##    

lang_dict = dict()
for (ielem, aelem) in zip(istr, astr):
    print "---------------------------------------------------"
    for (i,j) in zip(aelem, ielem):
        if i not in lang_dict.keys():
            lang_dict[i] = list()
        
        lang_dict[i] = j
lang_dict['z'] = 'q'
lang_dict['q'] = 'z'
lang_dict[' '] = ' '

##for i in sorted(lang_dict.keys()):
##    print i, '\t:\t', lang_dict[i]

def get_translation(line):
    answer = ""
    for i in line:
        answer = answer + lang_dict[i]
    return answer
def main():
    ifile = open('input', 'r')
    ofile = open('output', 'w')
    ite = 0
    for line in ifile:
        #To remove the first line, '100'
        if ite == 0:
            ite = ite + 1
            continue
        
        #strip newline
        line = line[:-1]
        answer = get_translation(line)
        ofile.write('Case #' + str(ite) + ': ' + answer + '\n')
        ite = ite + 1

if __name__ == '__main__':
    main();
