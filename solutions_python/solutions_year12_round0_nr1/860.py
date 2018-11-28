f = open('a-small-attempt0.in', 'r')
a = open('out.txt', 'w')

coded = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
decoded = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
decoder = {}
for i in range(len(coded)):
    decoder[coded[i]] = decoded[i]
decoder['q'] = 'z'
decoder['z'] = 'q'

for i in range(int(f.readline().strip())):
    in_str = f.readline().strip()
    result = ''
    for letter in in_str:
        result += decoder[letter]
    a.write("Case #" + str(i+1) + ": " + result + "\n")
    print "Case #" + str(i+1) + ": " + result
	
f.close()
a.close()
