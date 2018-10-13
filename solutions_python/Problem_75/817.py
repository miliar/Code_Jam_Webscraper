'''
Created on 06/mag/2011

@author: Luca Pinello

INPUT
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW


OUTPUT
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []

'''
fout=open('magicka_output.txt','w+')
fin=open('./input.txt','r')

if __name__ == '__main__':

    T=int(fin.readline())    
    for i in range(T):

        line=fin.readline()
        fields=line.split()
        
        C=int(fields[0])
        fields=fields[1:]
        
        combine_rules=fields[0:C]
        fields=fields[C:]
        
        D=int(fields[0])
        fields=fields[1:]
        
        clear_rules=fields[0:D]
        fields=fields[D:]

        N=int(fields[0])
        fields=fields[1:]
        
        string_to_parse=fields[0]
        fields=fields[N:]
        
        comb_reg=dict()
        clear_reg=dict()
        
        for rule in combine_rules:
            comb_reg[rule[0:2]]=rule[-1]
            comb_reg[rule[0:2][::-1]]=rule[-1]
        
        for rule in clear_rules:
            clear_reg[rule]=''
            clear_reg[rule[::-1]]=''
            
        modified=True
        computed_string=string_to_parse[0:2]
        string_to_parse=string_to_parse[2:]
        
        while modified or string_to_parse:
            modified=False

            for key in comb_reg.keys():
                if key == computed_string[-2:]:
                    computed_string = computed_string[:-2]+comb_reg[key]
                    modified=True
            
            for key in clear_reg.keys():
                if key[0] in computed_string and key[1] in computed_string:
                    computed_string = ''
                    modified=True
            
            if string_to_parse:
                computed_string+=string_to_parse[0]
                string_to_parse=string_to_parse[1:]
                modified=True
        
        if computed_string:
        
            s='['
            for c in computed_string:
                s+=c+', '
            s=s[0:-2]+']'
        else:
            s='[]'
        
        fout.write( 'Case #%d: %s\n' %(i+1, s)) 


fin.close()
fout.close()