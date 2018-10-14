import sys
t={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','z':'q','q':'z'}



d = open("C:\Python31\A-small-attempt0.in")
data = d.readline().strip('\r\n');
n = data
n = int(n)

st = d.readline().strip('\r\n')
i=0
while st !='':        
    sys.stdout.write("\nCase #" + str(i + 1)+ ": ")	
    for j in range(len(st)):sys.stdout.write(t[st[j]])		
#    sys.stdout.write("\n")	
    i= i + 1
    st = d.readline().strip('\r\n')

    
    
		
		