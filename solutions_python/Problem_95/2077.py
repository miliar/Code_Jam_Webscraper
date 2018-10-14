mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q', ' ': ' ', '\n': '\n'}
lines = open("A-small-attempt2.in").readlines()
out = open("out.txt","w")
x = 1
for line in lines[1:]:
    ans = "".join(map(lambda x: mapping[x], line))
    write = "Case #%d: %s" % (x,ans)
    out.write(write)
    x += 1
out.close
    
