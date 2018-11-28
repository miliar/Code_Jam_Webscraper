import sys
readin=sys.stdin.readline
english="abcdefghijklmnopqrstuvwxyz "
googlerese="ynficwlbkuomxsevzpdrjgthaq "
T=input()
for i in range(T):
	text=readin()
	text=text[:-1]
	trans=' '
	for j in range(len(text)):
		trans=trans+english[googlerese.find(text[j])]
	print 'Case #' + str(i+1) +':'+ trans
