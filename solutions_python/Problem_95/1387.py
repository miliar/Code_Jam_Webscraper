
mapping = {};

I="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z"
O="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q"

for i in range(len(I)):
	mapping[I[i]]=O[i];


Ls = iter(map(lambda l:l.strip(),open("A-small-attempt0.in").readlines()));

N = int(next(Ls));

for C in range(1,N+1):
	L = next(Ls);
	print("Case #%d: %s"%(C,"".join(map(lambda c:mapping[c],L))))
