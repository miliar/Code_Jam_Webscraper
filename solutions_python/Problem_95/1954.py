

class Fichier:
	def __init__(self,path):
		self.path = path
		self.fichier = None

	def open(self,option):
		try:
			self.fichier = open(self.path,option)
		except:
			print("Error File doesn't exist !!!")

	def close(self):
		self.fichier.close()

	def read(self):
		self.open('r')
		text = self.fichier.read()
		self.close()
		return text

	def write(self,text):
		self.open('a')
		self.fichier.write(str(text))
		self.close()
	def new_line(self):
		self.write('\n')

def tongues() :
	fichierin = Fichier("A-small.in")
	fichier = Fichier("output.out")
	i=fichierin.read()
	list=i.split("\n")
	i=int(list[0])
	p=1
	while p <= i:
		chaine=list[p]
		fichier.write("Case #")
		fichier.write(str(p))
		fichier.write(": ")
		for lettre in chaine:
			if lettre==" ":
				fichier.write(" ")
			if lettre=="a":
				fichier.write("y")
			if lettre=="b":
				fichier.write("h")
			if lettre=="c":
				fichier.write("e")
			if lettre=="d":
				fichier.write("s")
			if lettre=="e":
				fichier.write("o")
			if lettre=="f":
				fichier.write("c")
			if lettre=="g":
				fichier.write("v")
			if lettre=="h":
				fichier.write("x")
			if lettre=="i":
				fichier.write("d")
			if lettre=="j":
				fichier.write("u")
			if lettre=="k":
				fichier.write("i")
			if lettre=="l":
				fichier.write("g")
			if lettre=="m":
				fichier.write("l")
			if lettre=="n":
				fichier.write("b")
			if lettre=="o":
				fichier.write("k")
			if lettre=="p":
				fichier.write("r")
			if lettre=="q":
				fichier.write("z")
			if lettre=="r":
				fichier.write("t")
			if lettre=="s":
				fichier.write("n")
			if lettre=="t":
				fichier.write("w")
			if lettre=="u":
				fichier.write("j")
			if lettre=="v":
				fichier.write("p")
			if lettre=="w":
				fichier.write("f")
			if lettre=="x":
				fichier.write("m")
			if lettre=="y":
				fichier.write("a")
			if lettre=="z":
				fichier.write("q")
		fichier.new_line()
		p=p+1
	
	
def main() :
	 tongues()
main()
