'''
Created on Apr 14, 2012

@author: maka6er
'''

def mapping(string1, string2):
    mapping = {}
    for i in range(0, len(string1)):
        if string1[i] != ' ':
            if string1[i] in mapping and mapping[string1[i]] != string2[i]:
                print 'collision for: ' + string1[i]
            else:
                mapping[string1[i]] = string2[i]
    return mapping

def merge(mapping1, mapping2):
    result = mapping1
    for key in mapping2:
        if key not in result:
            result[key] = mapping2[key]
    return result

def alphabet(mapping):
    alphabet = []
    missing = []
    values = []
    corresponding = []
    
    key = 'a'
    for i in range(ord('a') + 1, ord('a') + 27):
        if key in m:
            alphabet.append(key);
            values.append(key)
        else:
            missing.append(key);
        key = chr(i)

    key = 'a'
    for i in range(ord('a') + 1, ord('a') + 27):
        if key not in values:
            corresponding.append(key)
        key = chr(i)

    return alphabet, missing, corresponding
    

#'a' -> 'y', 'o' -> 'e', 'z' -> 'q'

def translate(string, mapping):
    result = []

    for ch in string:
        if ch in mapping:
            result.append(mapping[ch])
        else:
            if ch == ' ':
                result.append(ch)
            else:
                result.append('-');
    
    return ''.join(result)


#ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv

T = 0
lines = []
input_file = open ('Speaking_in_Tongues.input', 'r')
line_number = 0
for line in input_file.readlines():
    if line_number == 0:
        T = int(line)
    else:
        lines.append(line.rstrip('\n'))
    line_number += 1

translated = ['our language is impossible to understand', 'there are twenty six factorial possibilities',
              'so it is okay if you want to just give up']

m1 = mapping(lines[0], translated[0])
m2 = mapping(lines[1], translated[1])
m = merge(m1, m2)
m3 = mapping(lines[2], translated[2])
m = merge(m, m3)

mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
           'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i',
           'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
           'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w',
           'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q' : 'z', 'z' : 'q'}

line_number = 1
for line in lines:
    print 'Case #' + str(line_number) + ': ' + translate(line, mapping)
    line_number += 1 
