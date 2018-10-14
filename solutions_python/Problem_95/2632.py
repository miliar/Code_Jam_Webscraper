#read
try:
    fi = open('input.txt','r')
    de = open('decoded.txt','r')
    co = open('coded.txt','r')
    try:
        lines = fi.readlines()
        decoded = de.readlines()
        coded = co.readlines()

    finally:
        fi.close()
        de.close()
        co.close()


except IOError:
    print 'file not found'

#write

def write_to_file(string, caseno):
    fo = open("output.txt", "a")
    fo.write('Case #'+str(caseno)+': '+ string+'\n')
    fo.close()

l = int(lines[0][0])
del lines[0:1]
print l

#missin q + z Q->z and z->q
dict = {}
dict['q'] = 'z'
dict['z'] = 'q'
i2 = 0
for b in decoded:
    i = 0
    for a in b:
        if a != ' ':
            if a not in dict:
                dict[a] = coded[i2][i]
        i+=1
    i2 += 1
print dict

case = 1
for e in lines:
    out = ''
    for f in e:
        if f == ' ':
            out += ' '
        elif f == '\n':
            a3 = 0
        else:
            out += dict[f]
    write_to_file(out,case)
    case+=1
        
