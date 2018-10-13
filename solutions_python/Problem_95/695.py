#!/usr/bin/python

#abeceda = [chr(x) for x in range(ord('a'),ord('z') + 1)]

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

trl = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']
#trl = ['#' for x in abc]
##n = input()

#orig = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

#novi = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'


#for i in range(len(orig)):
#	for j in range(len(abc)):
#		if orig[i] == abc[j]:
#			trl[j] = novi[i]
#	
#print(trl)

n = int(input())

ulaz = []

for i in range(n):
	ulaz.append(input())

izlaz = []

for ul in ulaz:
	s = ''
	for c in ul:
		if c == ' ':
			s = s + c
		else:
			for i in range(len(abc)):
				if (c == abc[i]):
					s = s + trl[i]
	izlaz.append(s)


for i in range(n):
	print('Case #' + str(i + 1) + ':',izlaz[i])

