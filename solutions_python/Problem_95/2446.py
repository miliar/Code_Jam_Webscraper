#create dictionary

goog = "y qee\n\
ejp mysljylc kd kxveddknmc re jsicpdrysi\n\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n\
de kr kd eoya kw aej tysr re ujdr lkgc jv"

eng = "a zoo\n\
our language is impossible to understand\n\
there are twenty six factorial possibilities\n\
so it is okay if you want to just give up"

eng_chars = []
goog_chars = []
for c in "abcdefghijklmnopqrstuvwxyz":
	goog_chars.append(c)
	eng_chars.append(c)

dict = {}
for i in range(len(eng)):
	if(goog[i] not in dict.keys()):
		dict[goog[i]] = eng[i]
	elif(dict[goog[i]] != eng[i]):
		raise Exception("language inconsistent: [{}] could be [{}] or [{}]".format(goog[i], dict[goog[i]], eng[i]))
		
	if(eng[i] in eng_chars):
		eng_chars.remove(eng[i])
	if(goog[i] in goog_chars):
		goog_chars.remove(goog[i])
		
if(len(goog_chars) == 1):
	dict[goog_chars[0]] = eng_chars[0]
elif(len(goog_chars) > 1):
	raise Exception("too many unknowns")

	
# read file

f = open('A-small-attempt0.in', 'r')
T = int(f.readline())
for i in range(T):
	G = f.readline()[:-1]
	O = "Case #{}: ".format(i+1)
	for c in G:
		O += (dict[c])
	print O