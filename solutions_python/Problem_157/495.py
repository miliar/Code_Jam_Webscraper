import re

debug = False

def deprint(msg):
    if debug:
        print msg

def preprocess(input_data1, input_data2):
    result = {}
    rests = input_data1.split(" ")
    #result['L'] = rests[0]
    X = int(rests[1])
    result['X'] = X % 4 + (4 if X >= 4 else 0)
    result['string'] = input_data2

    deprint(result)
    return result

table = {
    '11': '1',
    '1i':   'i',
    '1j':   'j',
    '1k':   'k',

    'i1':   'i',
    'ii':   '-1',
    'ij':   'k',
    'ik':   '-j',

    'j1':   'j',
    'ji':   '-k',
    'jj':   '-1',
    'jk':   'i',

    'k1':   'k',
    'ki':   'j',
    'kj':   '-i',
    'kk':   '-1'

}

def algo(pd):
    result = False

    #L = pd['L']
    X = pd['X']
    string = pd['string']
    data = "".join([string]*X)

    deprint(string)

    val = data[0]
    for char in data[1:len(data)]:
        val = mul(val, char)

        
    if val == "-1":
        deprint("val == -1")
        i_idx = find_i(data)
        if i_idx >= 0:
            k_idx = find_k(data)
            if k_idx >= 0 and k_idx > i_idx:
                result = True

    return result

def find_i(data):
    i = 0
    char = data[i]
    while i < (len(data) - 2) and char != 'i':
        i += 1
        char = mul(char, data[i])
    if char != 'i':
        i = -1
    return i

def find_k(data):
    i = len(data)-1
    char = data[i]
    while i > 2 and char != 'k':
        i -= 1
        char = mul(data[i], char)
    if char != 'k':
        i = -1
    return i

def mul(str1, str2):
    neg = 0
    if "-" in str1:
        neg = neg + 1
        str1 = re.sub("-","",str1)

    if "-" in str2:
        neg = neg + 1
        str2 = re.sub("-","",str2)

    result = table[str1+str2]
    if neg == 1:
        if "-" in result:
            result = re.sub("-","",result)
        else:
            result = "-" + result
    return result

def answer(ro, i):
    result = "Case #%d: %s" %(i+1, "YES" if ro else "NO")
    deprint("result: " + result)
    return result

"""main"""

N = int(raw_input())
deprint("N: %d" %N)

result = []
out = ''

for i in range(0, N):
    result.append( answer( algo( preprocess(raw_input(), raw_input()) ), i) )

deprint("=================")
out = '\n'.join(result)
print out

