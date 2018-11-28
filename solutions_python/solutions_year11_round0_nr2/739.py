import sys

def combine(li, el1, el2, el3):

    n = len(li)
    if (li[n-1] == el1 and li[n-2] == el2) or (li[n-1] == el2 and li[n-2] == el1):
        del li[n-1]
        del li[n-2]
        li.append(el3)

def oppose(li, el1, el2):

    n = len(li)
    if (li[n-1] == el1):
        try:
            num = li.index(el2)
            del li[0:n]
            #li = []
        except:
            #print 'hoge'
            num = -1

    elif (li[n-1] == el2):
        try:
            num = li.index(el1)
            del li[0:n]
            #li = []
        except:
            #print 'hoge'
            num = -1


n = int(raw_input(''))
for i in range(n):
    line = raw_input('')
    li = []
    combine_rule = []
    opposed = []
    invoke = []

    a = line.split()
    combine_num = int(a[0])
    if combine_num:
        combine_rule = list(a[1])
        opposed_num = int(a[2])
        if opposed_num:
            opposed = list(a[3])
            invoke_num = int(a[4])
            invoke = list(a[5])
        else:
            invoke_num = int(a[3])
            invoke = list(a[4])
    else:
        opposed_num = int(a[1])
        if opposed_num:
            opposed = list(a[2])
            invoke_num = int(a[3])
            invoke = list(a[4])
        else:
            invoke_num = int(a[2])
            invoke = list(a[3])

    for j in range(invoke_num):
        li.append(invoke[j])
        if combine_num and len(li)>1:
            combine(li, combine_rule[0], combine_rule[1], combine_rule[2])
        if opposed_num and len(li)>1:
            oppose(li, opposed[0], opposed[1])
        #print li

    print '''Case #%d: %s''' % (i+1, str(li).replace('\'', ''))
