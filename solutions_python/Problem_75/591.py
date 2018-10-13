#!/usr/bin/python
from sys import argv


def invoke(combinations, opposed, elements):
    spell=''
    opp_elements=[]
    i=0
    while i <len(elements):
        if opp_elements != []:
            if elements[i] in opp_elements:
                spell=''
                opp_elements.remove(elements[i])
            elif i<len(elements)-1:
                if elements[i:i+2] in combinations:
                    spell+=combinations[elements[i:i+2]]
                    i+=1
                elif elements[i] in opposed:
                    if opposed[elements[i]] in opp_elements:
                        spell+=elements[i]
                    else:
                        opp_elements.append(opposed[elements[i]])
                        spell+=elements[i]
                else:
                    spell+=elements[i]
            else:
                spell+=elements[i]
        else:
            if i<len(elements)-1:
                if elements[i:i+2] in combinations:
                    spell+=combinations[elements[i:i+2]]
                    i+=1
                elif elements[i] in opposed:
                    opp_elements.append(opposed[elements[i]])
                    spell+=elements[i]            
                else:
                    spell+=elements[i]
            else:
                spell+=elements[i]
        i+=1
    if len(spell) == 0:
        return '[]'
    elif len(spell) == 1:
        return '['+spell+']'
    else:
        spell_string='['
        for c in spell[0:-1]:
            spell_string+=c+', '
        spell_string+=spell[-1]+']'
        return spell_string


def magicka(input_file, output_file):
    f=open(input_file, 'r')
    N=int(f.readline())
    g=open(output_file, 'w')
    for i in xrange(N):
        line_list=(f.readline()).split(' ')
        n_comb=int(line_list.pop(0))
        combinations={}
        for j in xrange(n_comb):
            x=line_list.pop(0)
            combinations[x[0:2]]=x[2]
            combinations[x[1]+x[0]]=x[2]
        n_opposed=int(line_list.pop(0))
        opposed={}
        for j in xrange(n_opposed):
            x=line_list.pop(0)
            opposed[x[0]]=x[1]
            opposed[x[1]]=x[0]
        elements=line_list[-1].strip('\n')
        g.write('Case #'+str(i+1)+': ')
        invocation=invoke(combinations, opposed, elements)
        g.write(invocation+'\n')
    f.close()
    g.close()


#run: python magicka.py input output
if __name__=='__main__':
    if argv[0].find('magicka.py')!=-1:
        if len(argv)>=3:
            magicka(argv[1], argv[2])
