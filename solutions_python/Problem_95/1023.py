__author__ = 'Xiao Qian'

def speak_in_tongue(filename, mapping, output_tag):
    f = open(filename, 'r')
    output= open(output_tag+'_output.txt','w')
    num_of_case = int(f.readline())
    for caseid in range(num_of_case):
        tongue = f.readline().split('\n')[0]
        english = ''
        for letter in tongue:
            english += mapping[letter]


        output.write('Case #'+str(caseid+1)+': '+english+'\n')

    f.close()
    output.close()

if __name__ == '__main__':
    alphabet = set(map(chr, range(97,123)))
    exp1_eng = 'our language is impossible to understand'
    exp1_tongue = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    exp2_eng = 'there are twenty six factorial possibilities'
    exp2_tongue = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    exp3_eng = 'so it is okay if you want to just give up'
    exp3_tongue = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

    mapping = dict(zip(exp1_tongue+exp2_tongue+exp3_tongue,exp1_eng+exp2_eng+exp3_eng))

#    mapping.update(dict(zip(exp2_eng, exp2_tongue)))
    mapping.update({'q':'z'})
    missing_key = alphabet-set(mapping.keys())
    missing_value = alphabet - set(mapping.values())
    mapping.update({missing_key.pop():missing_value.pop()})
#    for letter in sorted(mapping):
#        print letter,': ', mapping[letter]
#    print len(mapping.keys())

    speak_in_tongue('A-small-attempt0.in', mapping, 'speaking_small')





  