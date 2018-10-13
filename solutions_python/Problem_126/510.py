cases = int(input())
cc=1
while cc<=cases:
	line = input().split()
	text = line[0]
	k = int(line[1])
	i=0
	count=0
	while i<len(text):
		j=i
		while j<len(text):
			c=i
			cons=0
			constart=c
			conend=c
			while c<=j:
				ff=ord(text[c]) 
				if ff!=ord('a') and ff!=ord('e') and ff!=ord('i') and ff!=ord('o') and ff!=ord('u'):
					conend+=1
				else:
					constart=c
					conend=c
					
				if conend-constart>=k:
					count+=1
					break;
				c+=1
			j+=1
			
		i+=1
	print ("Case #%d: %d"%(cc,count))
	cc+=1