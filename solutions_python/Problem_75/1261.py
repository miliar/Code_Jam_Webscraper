import string

inp = open('B-small-attempt1.in','r')
out = open('output.txt', 'w')

lines = inp.readlines()

def invoke(c, o, invoked):
    '''This function gets the joj done.'''

    cd = {}
    for i in range(0,len(c),3):
        cd[c[i] + c[i+1] if c[i] < c[i+1] else c[i+1] + c[i]] = c[i+2]

    ol = []
    for i in range(0,len(o),2):
        ol.append(o[i])
        ol.append(o[i+1])
        ol.append(o[i])

    ol2 = []

    il = []
    for i in invoked:
        booljon = False
        il.append(i)
        if len(il) > 1:
            cpair = il[-1] + il[-2] if il[-1] < il[-2] else il[-2] + il[-1]
            if cpair in cd:
                booljon = True
                il.pop()
                last = il.pop()
                il.append(cd[cpair])
                if last in o:
                    ol2.remove(ol[ol.index(last)+1])
                        
        if i in o and not booljon:
            ol2.append(ol[ol.index(i)+1])
            if i in ol2:
                il = []
                ol2 = []
        elif il[-1] in o:
            ol2.append(ol[ol.index(il[-1])+1])
            if il[-1] in ol2:
                il = []
                ol2 = []

            
    return il

def find_index(s):
    booljon = False
    for i in range(len(s)):
        if s[i] != ' ':
            booljon = True
        else:
            if booljon:
                return i

def format_string(s):
    s = s + ' '
    l = []
    while s != ' ':
        k = find_index(s)
        l.append(string.replace(s[0:k], ' ', ''))
        s = s[k:]
    return l
        
    

for i in range(1,len(lines)):
    line = lines[i]
    first = True if line[0] == '0' else False
    line = string.replace(line, ' ', '')
    for j in range(len(line)):
        if line[j].isdigit():
            line = string.replace(line, line[j], ' ')
    strings = format_string(line)

    invoked = strings.pop()[:-1]

    if len(strings) == 2:
        o = strings.pop()
        c = strings.pop()
    elif len(strings) == 1:
        if first:
            o = strings.pop()
            c = ''
        else:
            o = ''
            c = strings.pop()
    else:
        c = ''
        o = ''

##    c = string.replace(c, ' ', '')
##    o = string.replace(o, ' ', '')
##    invoked = string.replace(invoked, ' ', '')[:-1]

    print c, o, invoked
    result = invoke(c,o,invoked)
    final = 'Case #' + str(i) + ': ' + str(result) + '\n'
    final = string.replace(final, '\'', '')
    out.write(final)
