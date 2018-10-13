
mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 
    'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 
    'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 
    's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 
    'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}
    
def translate(text, mapping):
    return ''.join([mapping[char] for char in text])
    
n = int(input())
for i in range(n):
    text = input()
    print('Case #%d: %s' % (i+1, translate(text, mapping)))
