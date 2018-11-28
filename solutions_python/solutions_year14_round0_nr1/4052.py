def magic_trick (l1, l2):
    '''(list, list) -> str

    Return the result of a trick. 

    Precondition: len(l1) == len(l2)

    >>> magic_trick([1, 2, 3, 4], [4, 5, 6, 7])
    4
    '''

    num_matches = 0
    value = 0

    for i in range(len(l1)):
        for k in range(len(l2)):
            if l1[i] == l2[k]:
                num_matches = num_matches + 1
                value = l2[k]
                       
    if num_matches == 0:
        statement = 'Volunteer cheated!'
    elif num_matches == 1:
        statement = value
    else:
        statement = 'Bad magician!'
    
    return statement

import os
f = open(os.path.expanduser("/Users/perecmerec/Documents/Python/new.txt"), 'r')

n = int(f.readline())
print(n)

d1 = 0
d2 = 0
draft1 = 0
draft2 = 0
row1 = 0
row2 = 0
content = f.readlines()

for case in range(1,(n+1)):
    array1 = []
    array2 = []
    d1 = content[(2+10*(case-1)-2)]
    d2 = content[(7+10*(case-1)-2)]
    d1.strip('\n')
    d2.strip('\n')
    
    row1 = int(d1)
    row2 = int(d2)
    q = 0
    p = 0
    dupl = ''
    dapl = ''

    draft1 = str(content[((2+10*(case-1)-2) + row1)])
    draft2 = str(content[((7+10*(case-1)-2) + row2)])
    draft1 = draft1.strip('\n')
 #   draft1 = draft1.replace(' ', '')
    draft2 = draft2.strip('\n')
 #   draft2 = draft2.replace(' ', '')
 #   print(draft1,draft2)
    for h in range(len(draft1)):        
        if (h+q) < len(draft1):
            if draft1[h+q] != ' ':
                if (h+q+1) < len(draft1):
                    if draft1[h+q+1] == ' ':
                        array1.append(int(draft1[h+q]))
                    else:
                        dupl = draft1[h+q] + draft1[h+q+1]
                        array1.append(int(dupl))
                        q = q+1
                else:
                    array1.append(int(draft1[h+q]))

    for s in range(len(draft2)):        
        if (s+p) < len(draft2):
            if draft2[s+p] != ' ':
                if (s+p+1) < len(draft2):
                    if draft2[s+p+1] == ' ':
                        array2.append(int(draft2[s+p]))
                    else:
                        dapl = draft2[s+p] + draft2[s+p+1]
                        array2.append(int(dapl))
                        p = p+1
                else:
                    array2.append(int(draft2[s+p]))

        
    print('Case #'+str(case)+':', magic_trick(array1, array2))

    #print(d1,d2)

    #print(row1,row2)
    #print(array1,array2)
    #номера нужных рядов array1 и array2 искать по формуле (2+10*(case-1)) + row1 и
    # (7+10*(case-1)) + row2
    #значения array1 и array2 есть списки l1 и l2
    




f.close()
