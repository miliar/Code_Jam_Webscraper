import sys
map = {}
str1 = ["yqee", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
str2 = ["azoo", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

str1 = "".join(str1)
str2 = "".join(str2)

for i in range(len(str1)):
        map[str1[i]] = str2[i]

x = [0] * 26

#for i in range(len(str2)):
#        if(str2[i] != ' '):
#                x[ord(str2[i])-97] = 1
#for i in range(26):
#        print "%c: %d" % ((97+i), x[i])

map['z'] = 'q'

n = int(raw_input())
for i in range(n):
        sys.stdout.write("Case #%d: " % (i+1))
        str = raw_input()
        for j in range(len(str)):
                sys.stdout.write(map[str[j]]) 
        sys.stdout.write("\n")
