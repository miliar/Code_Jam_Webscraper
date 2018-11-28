x= 15
y = 26
maping = [25,14,6,9,3,23,12,2,11,21,x,13,24,19,5,22,y,16,4,18,10,7,20,8,1,17]

f = open("C:/Documents and Settings/Snuderl/Desktop/file.txt")
input = f.read().split("\n")
input = input[1:len(input)]
print input

r=""
for i,line in enumerate(input):
	r+="Case #"+(str(i+1))+": "
	for l in line:
		try:
			r+=chr(maping.index(ord(l)-96)+97)
		except:
			r+=l
	r+="\n"

print r

g = open("C:/Documents and Settings/Snuderl/Desktop/result.txt", "r+")
g.write(r)

print chr(maping.index(ord("a")-96)+97)