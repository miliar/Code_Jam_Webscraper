#coding=utf-8

from __future__ import with_statement
import string

class Hora:
	def __init__(self, h, m):
		if h < 24:
			self.hora = h
		else:
			self.hora = h - 24
		if m < 60:
			self.min = m
		else:
			self.min = m - 60
			self.hora += 1
			if self.hora >= 24:
				self.hora -= 24
	def __add__(self, outro):
		res = Hora(0,0)
		res.hora = self.hora + outro.hora
		res.min = self.min + outro.min
		if res.min >= 60:
			res.min -= 60
			res.hora += 1
		if res.hora >=24:
			res.hora -= 24
		return res
	def __sub__(self, outro):
		res = Hora(0,0)
		res.hora = self.hora - outro.hora
		res.min = self.min - outro.min
		if res.min < 0:
			res.min += 60
			res.hora -= 1
		if res.hora < 0:
			res.hora += 24
		return res
	def __eq__(self, outro):
		if self.hora == outro.hora:
			if self.min == outro.min:
				return True
			else:
				return False
		else:
			return False
	def __ne__(self, outro):
		return not (self == outro)
	def __gt__(self, outro):
		if self.hora > outro.hora:
			return True
		elif self.hora == outro.hora:
			if self.min > outro.min:
				return True
			else:
				return False
		else:
			return False
	def __lt__(self, outro):
		if self.hora < outro.hora:
			return True
		elif self.hora == outro.hora:
			if self.min < outro.min:
				return True
			else:
				return False
		else:
			return False
	def __ge__(self, outro):
		if self.hora > outro.hora:
			return True
		elif self.hora == outro.hora:
			if self.min >= outro.min:
				return True
			else:
				return False
		else:
			return False
	def __le__(self, outro):
		if self.hora < outro.hora:
			return True
		elif self.hora == outro.hora:
			if self.min <= outro.min:
				return True
			else:
				return False
		else:
			return False
	def __repr__(self):
		return "< " + self.__str__() + " >"
	def __str__(self):
		return str(self.hora).zfill(2) + ":" + str(self.min).zfill(2)

class Trem:
	def __init__(self, h, m):
		self.disponivel = True
		self.hora = Hora(h, m)
	def __repr__(self):
		return self.hora.__str__()

def comp(x, y):
	if x.hora < y.hora:
		return -1
	elif x.hora == y.hora:
		return 0
	else:
		return 1


if __name__ == "__main__":
	with open("B-small.in") as arq:
		N = int(arq.readline())

		for caso in xrange(1,N+1):
			#tempo de "turnaround"
			T = int(arq.readline())
			T = Hora(0, T)
			#numero de viagens entre A e B
			NA,NB = arq.readline().split(" ")
			NA = int(NA)
			NB = int(NB)
			#Trens que tem que sair de A e B, hora
			saida_A = []
			saida_B = []
			#trens livres em A e B, hora
			disp_A = []
			disp_B = []
			#numero de trens em A e B, inicialização
			num_A = 0
			num_B = 0
			#hora dos trens que tem que sair de A e B e a hora que estão disponíveis em A e B
			for i in xrange(NA):
				horas = arq.readline()
				horas = horas.split(" ")
				saida_A.append(Trem(int(horas[0].split(":")[0]),int(horas[0].split(":")[1])))
				disp_B.append(Trem(int(horas[1].split(":")[0]),int(horas[1].split(":")[1])))
				disp_B[i].hora = disp_B[i].hora + T
			for i in xrange(NB):
				horas = arq.readline()
				horas = horas.split(" ")
				saida_B.append(Trem(int(horas[0].split(":")[0]),int(horas[0].split(":")[1])))
				disp_A.append(Trem(int(horas[1].split(":")[0]),int(horas[1].split(":")[1])))
				disp_A[i].hora = disp_A[i].hora + T

			#ordena tudo pra "facilitar"
			saida_A.sort(cmp=comp)
			saida_B.sort(cmp=comp)
			disp_A.sort(cmp=comp)
			disp_B.sort(cmp=comp)
			#pega o primeiro disponivel em A e compara com as horários necessários
			if len(disp_A) != 0:
				for i in xrange(len(disp_A)):
					for j in xrange(i, len(saida_A)):
						if saida_A[j].disponivel == True and disp_A[i].disponivel == True:
							if disp_A[i].hora <= saida_A[j].hora:
								disp_A[i].disponivel = False
								saida_A[j].disponivel = False
								break
				for i in saida_A:
					if  i.disponivel == True:
						num_A += 1
			else:
				num_A = len(saida_A)
			#pega o primeiro disponivel em B e compara com os horários necessários
			if len(disp_B) != 0:
				for i in xrange(len(disp_B)):
					for j in xrange(i, len(saida_B)):
						if saida_B[j].disponivel == True and disp_B[i].disponivel == True:
							if disp_B[i].hora <= saida_B[j].hora:
								disp_B[i].disponivel = False
								saida_B[j].disponivel = False
								break
				for i in saida_B:
					if  i.disponivel == True:
						num_B += 1
#				min_B = disp_B[0]
#				for i in xrange(len(saida_B)):
#					if min_B > saida_B[i]:
#						num_B += 1
			else:
				num_B = len(saida_B)
		
			#imprime a saída, primeiro teste agora!!
			print "Case #%i: %i %i" % (caso, num_A, num_B) 			

