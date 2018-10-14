import re

vowels = ['a','e','i','o','u']

def get_nvalue(name, n):
    count = 0
    for i in range(len(name)):
        for j in range(n+i, len(name)+1):
            pat = "[^aeiou]{"+ str(n) + ",}"
            if re.search(pat, name[i:j]):
                count = count + 1
    return count


#f = open('A-large.in', 'r')
f = open('A-small-attempt0.in', 'r')

#f = open('practice.txt', 'r')

output = open('output.txt','w')

T = int(f.readline())

#print(T)

for i in range(1,T+1):
    line1 = f.readline().rstrip().split()
    #motes = [int(x) for x in f.readline().rstrip().split()]

    name = line1[0]
    n = int(line1[1])

    #print (name, n)

    result = get_nvalue(name,n)

    text = 'Case #'+str(i)+': '+ str(result)

    print(text,file=output)
    #print(text)

    #print()

f.close()
output.close()

#print(lines)
