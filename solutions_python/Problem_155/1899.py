def will(ch):
	j = 0
	for c in ch:
		if j == 0:
			wil = int(c)
		else:
			if wil >= j:
				wil += int(c)
		j+=1
	return wil

def present(ch):
	k = 0
	for c in ch:
		k += int(c)
	return k

def spli(ch):
	u = []
	for c in ch:
		u.append(int(c))
	return u

f = open("A-small-attempt1.in","r")
out = open("out.txt","w")
n=int(f.readline())
i = 0
for ligne in f.readlines() :
	i += 1
	ligne = ligne[:len(ligne)-1:]
	ligne = ligne.split(" ")
	stri = ligne[1]
	presents = present(stri) 
	willclap = will(stri)
	u = spli(stri)
	if presents == willclap:
		t = 1
	else:
		t = 0
	k = 0
	while t == 0:
		k += 1
		u[0] += 1
		s = ""
		for u1 in u:
			s += str(u1)
		if present(s) == will(s):
			t = 1

	final = "Case #"+ str(i) +": "+ str(k)+"\n"
	out.write(final)
	#print "\n"