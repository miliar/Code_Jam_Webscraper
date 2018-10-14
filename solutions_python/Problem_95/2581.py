key = {' ': ' ', 'a': 'y', 'b': 'h',
        'c': 'e', 'd': 's', 'e': 'o',
        'f': 'c', 'g': 'v', 'h': 'x',
        'i': 'd', 'j': 'u', 'k': 'i',
        'l': 'g', 'm': 'l', 'n': 'b',
        'o': 'k', 'p': 'r', 'q': 'z',
        'r': 't', 's': 'n', 't': 'w',
        'u': 'j', 'v': 'p', 'w': 'f',
        'x': 'm', 'y': 'a', 'z': 'q',
        }

def decode(s):
    result = ''
    for i in s:
        result += key[i]

    return result

input_file = open('input.txt','r')
test_cases = int(input_file.readline())
input_msg = input_file.readlines()
input_file.close()
output_file = open('output.txt','w')

for i in range(test_cases):
    output_file.write('Case #' + str(i+1) + ': ' + decode(input_msg[i].strip())+'\n')

output_file.close()
