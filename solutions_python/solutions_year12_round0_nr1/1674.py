dict1 = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

z = int(raw_input("enter number: "))
i = 2
while i<z:
    text = raw_input('Enter String: ')
    textsolution  = "Case #1: "
    for x in text:
        if(x == '\n'):
            textsolution += dict1[x]
            textsolution += "Case #" + str(i) + ": "
            i+=1
        else:
            textsolution += dict1[x]
            
    print textsolution
    
