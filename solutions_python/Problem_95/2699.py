# google dict was handmade.
google = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

file = open('./input', 'r')
data = ''
answer=list()
counter = 0
for line in file:
	if line[0] not in '0123456789': 
	     counter +=1
	     answer.append('Case #{0}: '.format(counter))
             for i in line:
                     if i != ' ' and i != '\n':
                             answer.append(google[i])
		     elif i == ' ':
			     answer.append(' ')
             answer.append('\n')
answer.pop(-1)
print ''.join(answer)