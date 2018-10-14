words={}

def search (position,key):
	if len(key)==0:
		return 1
	elif key[0]=="(":
		total=0
		for i in key[1:key.find(")")]:
			if i in position:
				total+=search(position[i],key[key.find(")")+1:])
		return total
	elif key[0] in position:
		return search(position[key[0]],key[1:])
	else:
		return 0

l,d,n=map(int,raw_input().split())
for i in xrange(d):
	new=raw_input()
	position=words
	for j in new:
		if j in position:
			position=position[j]
		else:
			position[j]={}
			position=position[j]
for i in xrange(n):
	print "Case #"+str(i+1)+":",search(words,raw_input())