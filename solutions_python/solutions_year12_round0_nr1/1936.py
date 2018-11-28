transl = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ': ' ', '\n':''}


with open('A-small-attempt0.in', 'r') as fp:
    x = int(fp.readline())
    for line, num in zip(fp,range(1,x+1)):
        out = "".join(map(lambda x: transl[x], line))
        print 'Case #' + str(num) + ':', out
    
