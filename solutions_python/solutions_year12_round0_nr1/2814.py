N = raw_input()

#  'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'.
s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" 
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
sm1 = "our language is impossible to understand"
sm2 = "there are twenty six factorial possibilities"
sm3 = "so it is okay if you want to just give up"
mapping = {}
s = [s1, s2, s3]   
sm = [sm1, sm2, sm3]

mapping['q'] = 'z'
mapping['z'] = 'q'
for k in range (0, len(s)):
    sample = s[k]
    sample_mapping = sm[k]
    for j in range (0, len(sample)): 
        if not sample[j] in mapping:
            mapping[sample[j]] = sample_mapping[j]


for i in range (0, int(N)):
    string = raw_input()
    for j in range (0, len(string)):
        string_list = list(string)
        string_list[j] = mapping[string[j]]
        string = "".join(string_list)
    print "Case #%d: %s" % (i+1, string) 
# 
# for j in range (0, len(mapping)):
#     print sorted(mapping)[j], "->", mapping[sorted(mapping)[j]]