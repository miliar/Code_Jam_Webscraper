Quaternion = {
    #_,o
    ('o','o'): 'o',
    ('i','o'): 'i',
    ('j','o'): 'j',
    ('k','o'): 'k',
    ('n','o'): 'n',
    ('x','o'): 'x',
    ('y','o'): 'y',
    ('z','o'): 'z',
    #_,i
    ('o','i'): 'i',
    ('i','i'): 'n',
    ('j','i'): 'z',
    ('k','i'): 'j',
    ('n','i'): 'x',
    ('x','i'): 'o',
    ('y','i'): 'k',
    ('z','i'): 'y',
    #_,j
    ('o','j'): 'j',
    ('i','j'): 'k',
    ('j','j'): 'n',
    ('k','j'): 'x',
    ('n','j'): 'y',
    ('x','j'): 'z',
    ('y','j'): 'o',
    ('z','j'): 'i',
    #_,k
    ('o','k'): 'k',
    ('i','k'): 'y',
    ('j','k'): 'i',
    ('k','k'): 'n',
    ('n','k'): 'z',
    ('x','k'): 'j',
    ('y','k'): 'x',
    ('z','k'): 'o',
    #_,n
    ('o','n'): 'n',
    ('i','n'): 'x',
    ('j','n'): 'y',
    ('k','n'): 'z',
    ('n','n'): 'o',
    ('x','n'): 'i',
    ('y','n'): 'j',
    ('z','n'): 'k',
    #_,x
    ('o','x'): 'x',
    ('i','x'): 'o',
    ('j','x'): 'k',
    ('k','x'): 'y',
    ('n','x'): 'i',
    ('x','x'): 'n',
    ('y','x'): 'z',
    ('z','x'): 'j',
    #_,y
    ('o','y'): 'y',
    ('i','y'): 'z',
    ('j','y'): 'o',
    ('k','y'): 'i',
    ('n','y'): 'j',
    ('x','y'): 'k',
    ('y','y'): 'n',
    ('z','y'): 'x',
    #_,z
    ('o','z'): 'z',
    ('i','z'): 'j',
    ('j','z'): 'x',
    ('k','z'): 'o',
    ('n','z'): 'k',
    ('x','z'): 'y',
    ('y','z'): 'i',
    ('z','z'): 'n',
}

def substring1(string):
    if len(string) < 3:
        return 'NO'
    for i in range(1, len(string)-1):
        sub1 = string[:i]
        if Checki(sub1):
            if substring2(string[i:]):
                return 'YES'
    return 'NO'

def substring2(string):
    for j in range(1, len(string)):
        sub2 = string[:j]
        if Checkj(sub2):
            if Checkk(string[j:]):
                return True
    return False

def Checki(string):
    if Check(string) == 'i':
        return True
    return False

def Checkj(string):
    if Check(string) == 'j':
        return True
    return False

def Checkk(string):
    if Check(string) == 'k':
        return True
    return False

def Check(string):
    while len(string) > 1:
        #string = string[0:-2] + Quaternion[(string[-2], string[-1])]
        for key in Quaternion.iterkeys():
            a, b = key
            string = string.replace(a+b, Quaternion[key])
            if len(string) == 1:
                break
    return string
    
input_file = open('C-small-attempt0.in', 'r')
source = input_file.read()
source = source.splitlines()
input_file.close()
output = open('output-C-small-attempt0.txt', 'w')
for i in range(int(source[0])):
    output.write('Case #%d: '%(i+1))
    values = source[(i+1)*2-1].split(' ')
    substring = source[(i+1)*2]
    string = source[(i+1)*2]*int(values[1])
    if len(set(substring))==1:
        answer = 'NO'
    elif Check(string) != 'n':
        answer = 'NO'
    else:
        answer = substring1(string)
    output.write(answer + '\n')
output.close()
