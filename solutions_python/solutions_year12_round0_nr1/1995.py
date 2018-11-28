import sys
import pdb
sys.path.append('D:/codejam/qualification round/A')

file = open('input.txt')
input = file.read()
file.close()

input = input.split("\n")

T = int(input[0])
input = input[1:]

result = []

file = open('mapping.txt')
mapping = file.read()
file.close()

def replace_letter(s):
    for mapping_component in mapping.split('\n'):
        if s == mapping_component.split(' ')[0]:
            return mapping_component.split(' ')[1]
    return ' '

for i in range(0,T):
    replaced = ''
    for character in input[0]:
        #pdb.set_trace()
        replaced = replaced + replace_letter(character)
    #pdb.set_trace()
    result += [replaced]
    input = input[1:]
    

file = open('output.txt', 'w')
for i in range(0,T):
    file.write('Case #'+str(i+1)+': '+result[i]+'\n')