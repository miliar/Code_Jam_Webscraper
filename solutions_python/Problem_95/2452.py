alpha_map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
           'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
           'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r',
           's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p',
           'y': 'a', 'x': 'm', 'z': 'q'}

T = int(raw_input())
for i in range(1,T+1):
    input_text =  str(raw_input())
    output = ""
    for j in range(0,len(input_text)):
        output = output + alpha_map[input_text[j]]
    print "Case #"+ str(i)+ ": " + output
