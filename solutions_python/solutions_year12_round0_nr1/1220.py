def translate(l, i):
    english =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    googlerese=['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']
    new_list = []
    
    for j in range(len(l)):
        word = l[j]
        chars = list(word)
        
        seperated_chars = []
        for k in range(len(chars)):
            pos = googlerese.index(chars[k])
            seperated_chars.append(english[pos])

        new_word = ''.join(seperated_chars)
        new_list.append(new_word)
            
    string = ' '.join(new_list)
    fout = open("output.txt", "a")
    fout.write("Case #" + str(i) + ": ")
    fout.write(string)
    fout.write("\n")
    fout.close()
        

fin = open("file.txt", "r")

n = int(fin.readline())
for i in range(n):
    line = fin.readline()
    l = line.split()
    translate(l, i+1)


