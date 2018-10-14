'''
Created on Apr 13, 2012

@author: redoacs
'''

input = 'A-small-attempt0.in'
output = 'A-small-attempt0.out'

examples_c = 'y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z'
examples_d = 'a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q'

test = 'abcdefghijklmnopqrstuvwxyz'

def buildMap(domain,codomain):
    function_map = {}
    
    for c,d in zip(domain, codomain) :
        #print(c, d)
        if c not in function_map:
            function_map[c] = d
        else:
            if not function_map[c] == d: 
                raise("Repeated and different mapping in examples")
    
    #print(function_map)
    return function_map


def translate(string, f_m):
    translated = ''
    for c in string:
        translated += f_m[c]
    return translated

if __name__ == '__main__':

#    cfm = buildMap(examples_d, examples_c)
    dfm = buildMap(examples_c, examples_d)
#    
#    print(examples_c)
#    print(translate(examples_c, dfm))
#    print(examples_d)
#    print(translate(examples_d, cfm))
#    
#    print(test)
#    print(translate(test, dfm))
#    print(test)
#    print(translate(test, cfm))
    
    input_file = open(input)
    output_file = open(output, 'w')
    ntc = int(input_file.readline());
    
    for i in range(ntc):
        tc = input_file.readline()[:-1]
        print(tc)
        print(translate(tc, dfm))
        print('Case #', i+1 , ": " , translate(tc, dfm) , sep='', file=output_file)
    
    