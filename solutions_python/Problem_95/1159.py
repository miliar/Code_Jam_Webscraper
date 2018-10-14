#A prob

import sets
if __name__ == '__main__':
    googlerese = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    normal = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
    mapping = sets.Set()
    for a, b in zip(googlerese,  normal):
        mapping.add((a, b))
    mapping.add(('q', 'z'))
    mapping.add(('z', 'q'))
    
    temp_list = list(mapping)
    mapping_dict = dict(temp_list)
    
    test_cases = int(raw_input())
    for test in range(test_cases):
        google = raw_input()
        normal_stmt = ''
        print 'Case #%d:'%(test+1),
        for charc in google:
            normal_stmt +=  mapping_dict[charc]
        print normal_stmt
    
    
