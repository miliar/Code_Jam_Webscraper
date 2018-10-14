import re

if __name__ == '__main__':
    f = open('c:\\A-large.in')
    fout = open('c:\\result.out', 'w')
    cletter,cword,cpattern = f.readline().strip().split()
    cletter=int(cletter)
    cword=int(cword)
    cpattern=int(cpattern)
    print cletter,cword,cpattern
    words = []
    patterns = []
    for i in range(cword):
        words.append(f.readline().strip())
    print words
    for i in range(cpattern):
        str_in = f.readline().strip()
        print str_in
        str_in = str_in.replace('()','')
        len_in = len(str_in)
        out = []
        in_parenthesis = False
        for j in range(len_in):
            if str_in[j] == '(':
                out.append(str_in[j])
                in_parenthesis = True
            elif str_in[j] == ')':
                out.pop()
                out.append(str_in[j])
                in_parenthesis = False
            else:
                out.append(str_in[j])
                if in_parenthesis:
                    out.append('|')
        str_out = '^'+''.join(out)+'$'
        print str_out
        r  = re.compile(str_out)
        mc = 0
        for word in words:
            if r.match(word) is None:continue
            mc+=1
        print 'Case #%d: %d'%(i+1,mc)
        fout.write('Case #%d: %d\n'%(i+1,mc))
    f.close()
    fout.close()
        