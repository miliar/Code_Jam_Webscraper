f1 = open('sample_in.txt')
f2 = open('sample_out.txt')

T = f1.next()
dictionary = {'q': 'z', 'y': 'a', 'e': 'o', 'z': 'q'}


for i in range(1,int(T)+1):
    ln1 = f1.next()
    ln2 = f2.next()
    for j in range(1,len(ln1)):
        dictionary[ln1[j]] = ln2[j]

print dictionary


foo = open('A-small')
#foo = open('sample_in.txt')
foo2 = open('out.txt', 'w')
cnt = 1
foo.next()
for line in foo:
    print line,
    string = 'Case #' + str(cnt) + ": "
    for ch in line:
        string = string + dictionary[ch]
    foo2.write(string)
    print(string),
    cnt += 1
foo.close()
foo2.close()
f1.close()
f2.close()
