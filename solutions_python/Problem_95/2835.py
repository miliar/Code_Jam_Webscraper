def map_me(line):
    out = ''
    for char in line:
        if char in mapping:
            out += mapping[char]
        else:
            out += char
    return out

file_in = open("A-small-attempt5.in")
file_out = open("output.out","w")

mapping = {'a':'y','b':'h','c':'e','d':'s','e':'o',
           'f':'c','g':'v','h':'x','i':'d','j':'u',
           'k':'i','l':'g','m':'l','n':'b','o':'k',
           'p':'r','q':'z','r':'t','s':'n','t':'w',
           'u':'j','v':'p','w':'f','x':'m','y':'a',
           'z':'q'}     
        
T =int(file_in.readline())

for i in range(T):
    s = map_me(file_in.readline().strip())
    file_out.write('Case #'+str(i+1)+': '+s+'\n')
    
file_out.close()
file_in.close()