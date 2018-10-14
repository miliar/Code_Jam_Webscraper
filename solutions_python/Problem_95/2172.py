mapping = {'a' : 'y' , 'o' : 'e' , 'z' : 'q', ' ': ' '}
inv_mapping = {}
def encode(str) :
    result = ''
    for c in str:
        result += mapping[c]
    return result


def decode(str) :
    result = ''
    for c in str:
        result += inv_mapping[c]
    return result

def create_mapping(code, text) :
    for i in range(len(text)) :
        c = text[i]
        if c in mapping :
            if mapping[c] != code[i] :
                print 'ERROR'
        else :
            mapping[c] = code[i]

    print "Number of mapped characters :" , len(mapping)

create_mapping("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
create_mapping("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
create_mapping("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")

create_mapping('z','q')

for c in mapping:
    inv_mapping[mapping[c]] = c

f = open('in1.txt', 'r')
alpha = [chr(i+ord('a')) for i in range(26)]
alpha2 = []
for c in alpha :
    try :
        alpha2.append(mapping[c])
    except : pass

n = int(f.readline())

for n in range(n) :
    l = f.readline()[:-1]
    print ("Case #{}: {}").format(1+n,decode(l))
    


f.close()
