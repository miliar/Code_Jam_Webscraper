import math

def palindromi(num):
	if (str(num) == str(num)[::-1]):
		return True
	return False

def ch(mini, maks):
	lkm = 0 
	testi = int(math.sqrt(mini))
	while (testi**2<=maks):
		if(testi**2>=mini and palindromi(testi**2) and palindromi(testi)):
			lkm += 1
		testi += 1
	return lkm


fin = open("c.in","r")
out=open("c.out","w")
count = int(fin.next())
for j in range(count):
	rivi=fin.next()
	minimi = int(rivi.split(" ")[0])
	maksimi = int(rivi.split(" ")[1])
	out.write("Case #{0}: {1}\n".format(j+1,ch(minimi,maksimi)))

fin.close()
out.close()
