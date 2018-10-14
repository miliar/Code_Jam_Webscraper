#!/usr/bin/env python

import sys, re

def buildAlphaBet(words) :
    letters = []
    for w in words :
        for let in w :
            if not let in letters :
                letters.append(let)
    return letters
    
r = re.compile('\\([^#]*?\\)')
def possibilitys(case,words,letters) :
    mp =  r.findall(case) #multiple possiblitys
    mp_iter = iter(mp)
    options = []
    i = 0
    while i < len(case) :
        if case[i] == '(' :
            m = mp_iter.next()
            options.append(m[1:-1])
            i = i + len(m)
        else :
            options.append(case[i])
            i = i + 1
    #print(case)
    #cleaning up
    #print(options)
    #building possibilitys
    p = []
    def buildtree(i,preS) :
        if i == 0 or preS in [w[0:i] for w in words] :
            for opt in options[i]:
                if opt in letters :
                    if i+1 < len(options) :
                        buildtree(i+1,preS+opt)
                    elif  preS+opt in words :
                        p.append(preS+opt)
    buildtree(0,'')
    #print(p)
    return(p)
                            

def analyse_data_file(datafile) :
    f = file(datafile)
    lines = f.readlines()
    L,D,N = [int(a) for a in lines[0].strip().split(' ')]
    print('L : %i, D: %i, N: %i'%(L,D,N))
    words = [w.strip() for w in lines[1:D+1]]
    cases = [w.strip() for w in lines[D+1:]]
    print(words, cases) 
    #building alphabet
    letters = buildAlphaBet(words)
    print('letters identified')
    print('  ' + ','.join(letters))
    #now analysis cases
    output = []
    for case,i in zip(cases,range(N)) :
        p = possibilitys(case,words,letters)
        #counting valid possiblities
        #matches = [wp in words for wp in p]
        outText = 'Case #%i: %i' %(i+1,len(p))#sum(matches))
        print(outText)
        output.append(outText)
    return output


output = analyse_data_file(sys.argv[1])
fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))

