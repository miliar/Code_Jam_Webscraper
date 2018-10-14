from string import ascii_lowercase

dic = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z','z':'q'}

n = int(raw_input())
case = 1
for i in xrange(n):
    g = raw_input()
    trans = ''
    for char in g:
      if char == ' ':
          trans += ' '
      else:
          trans += dic[char]
    print 'Case #%d: %s' %(case, trans)
    case+=1

