'''
Created on 2012-4-14

@author: Philip85517
'''

mapping_dict = dict()

def get_word_mapping(input, output, my_dict):
    input = input.split()
    output = output.split()
    for word in input:
        orig = output.pop(0)
        for i in range(0, len(word)):
           my_dict[word[i]] = orig[i]


input1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
input2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
input3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
ans1 = 'our language is impossible to understand'
ans2 = 'there are twenty six factorial possibilities'
ans3 = 'so it is okay if you want to just give up'

get_word_mapping(input1, ans1, mapping_dict)
get_word_mapping(input2, ans2, mapping_dict)
get_word_mapping(input3, ans3, mapping_dict)
mapping_dict['z'] = 'q'
mapping_dict['q'] = 'z'
mapping_dict[' '] = ' '
mapping_dict['\n'] = ''
#print mapping_dict.keys()
#print mapping_dict.values()



file_handle = open('A-small-attempt0.in')
#file_handle = open('small.in', "r")
T = int(file_handle.readline())
for i in range(0, T):
    line = file_handle.readline()
    result = []
    for k in range(0, len(line)):
        #print mapping_dict[line[k]]
        result.append(mapping_dict[line[k]])
    
    print "Case #%d: %s" % (i + 1, ''.join(result))

