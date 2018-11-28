testcases = int(input())

d = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(sentence):
    l_sentence = []
    for c in sentence:
        try:
            l_sentence.append(d[c])
        except KeyError:
            l_sentence.append(c)
    
    res = ''.join(l_sentence)
    
    return res


for i in range(1, testcases + 1):
    G = input()
    print('Case #' + str(i) + ': ' + translate(G))
