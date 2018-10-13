import sys

def war(naomi,ken):
	c = 0
	pn=0
	pk=0
	for i in range(0,len(naomi)):
		if naomi[pn] < ken[pk]:
			pn = pn + 1
			pk = pk + 1
		else:
			pk = pk + 1
			c = c + 1
	return c

def noWar(naomi,ken):
	c = 0
	pn=0
	pk=0
	for i in range(0,len(naomi)):
		if naomi[pn] < ken[pk]:
			pn = pn + 1
		else:
			pn = pn + 1
			pk = pk + 1
			c = c + 1
	return c

def main():
	i = 0
	j = 0
	caso=0
	for line in sys.stdin:
		i = i + 1
		if i != 1:
			j = j + 1
			if j != 1:
				if j == 2:
					naomi = line.split()
				if j == 3:
					caso=caso+1
					ken = line.split()
					naomi.sort()
					ken.sort()
					v1 = noWar(naomi,ken)
					v2 = war(naomi,ken)
					print(("Case #%i: %i %i")%(caso,v1,v2))
					j = 0
main()