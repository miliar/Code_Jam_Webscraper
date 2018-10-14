googlerese = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q', ' ': ' '}

def calc(case):
    result = ''
    for char in case:
        result += googlerese[char]

    print result
    return result




f = open('A-small.in', 'r')
lines = f.readlines()   
f.close()
c = lines[0].split()[0]
#print c     
cases = [r.strip() for r in lines[1:]]
#print cases  

of = open('output_a_small.txt', 'w')

for idx, case in enumerate(cases):
    of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(case)})                          

of.close()
