crypt   = {1:"ejp mysljylc kd kxveddknmc re jsicpdrysi",2:"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",0:"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
decrypt = {1:"our language is impossible to understand",2:"there are twenty six factorial possibilities",0:"so it is okay if you want to just give up"};
rules 	= {"q" : "z", "z" : "q"};

for i in range(3):
	print(i);
	
	for j in range(len(crypt[i])):
		rules[crypt[i][j]]	= decrypt[i][j]
		
	
print(rules);
print(len(rules));	
count = int(input())
for i in range(count):	
	res = "".join(list(map(lambda y:rules[y],input())))
	print("Case #"+str(i+1)+": "+res)