#!/usr/bin/env python

import sys
from math import *
 
class Quaternion:
 
	def __init__(self,a,b):
		self.a=a
		self.b=b
 
	def __str__(self):
		aff='('
		aff+=str(self.a.real)+')+('
		aff+=str(self.a.imag)+')i+('
		aff+=str(self.b.real)+')j+('
		aff+=str(self.b.imag)+')k'
		return aff

	def __repr__(self):
		return self.__str__()
 
	def __neg__(self):
		return Quaternion(-self.a,-self.b)
 
	def __add__(self,other):
		return Quaternion(self.a+other.a,self.b+other.b)
 
	def __sub__(self,other):
		return Quaternion(self.a-other.a,self.b-other.b)
 
	def __mul__(self,other):
		c=self.a*other.a-self.b*other.b.conjugate()
		d=self.a*other.b+self.b*other.a.conjugate()
		return Quaternion(c,d)
 
	def __rmul__(self,k):
		return Quaternion(self.a*k,self.b*k)
 
	def __abs__(self):
		return hypot(abs(self.a),abs(self.b))
 
	def conjugate(self):
		return Quaternion(self.a.conjugate(),-self.b)
 
	def __div__(self,other):
		return self*(1./abs(other)**2*other.conjugate())
 
	def __pow__(self,n):
		r=1
		for i in range(n):
			r=r*self
		return r

	def __eq__(self, other):
		return True if (self.a == other.a) and (self.b == other.b) else False


class q():
	@classmethod
	def i(self):
		return Quaternion(complex(0,1), complex(0,0))
	@classmethod
	def j(self):
		return Quaternion(complex(0,0), complex(1,0))
	@classmethod
	def k(self):
		return Quaternion(complex(0,0), complex(0,1))
	@classmethod
	def zero(self):
		return Quaternion(complex(0,0), complex(0,0))
	@classmethod
	def one(self):
		return Quaternion(complex(1,0), complex(0,0))


def can_ijk(nb):
	res=0
	tmp = []
	prev_ind=0
	occur=0

	for i in range(1, len(nb)+1):
		res = q.one()
		for p in nb[0:i]:
			res *= getattr(q, p)()
			if q.i() == res:
				if can_jk(nb[i:]):
					return True

		# Check pattern repetition
		for it, t in enumerate(tmp):
			if t == res:
				if prev_ind == it:
					tmp.remove(t)
					occur += 1
				prev_ind = it
		if occur >= 200:
			return False
		tmp.append(res)
	
	return False


def can_jk(nb):
	res=0
	for i in range(1, len(nb)+1):
		res = q.one()
		for p in nb[0:i]:
			res *= getattr(q, p)()
			if res == q.j():
				if can_k(nb[i:]):
					return True

def can_k(nb):
	res=0
	for i in range(1, len(nb)+1):
		res = q.one()
		for p in nb[0:i+1]:
			res *= getattr(q, p)()
			if res == q.k():
				return True

def is_minus_one(nb):
	res = q.one()
	for n in nb:
		res *= getattr(q, n)()
	return True if res == -q.one() else False

def one_letter(nb):
	return True if nb.count(nb[0]) == len(nb) else False


if __name__ == "__main__":

	if len(sys.argv) != 2:
		print "usage: " + sys.argv[0] + " input_file"
		exit(0)

	in_file = open(sys.argv[1], 'r').readlines()

	cases_nb = int(in_file[0].strip())

	# Removing line feed
	cases = [ in_file[i:i+2] for i in range(1,cases_nb*2,2)]
	for ic,c in enumerate(cases):
		for il,l in enumerate(c):
			c[il] = l.strip()

	sol = ""
	# For each cases
	for ic,c in enumerate(cases):
		chunk_size, repeat = c[0].split(' ')
		repeat = int(repeat)

		s = c[1]*repeat
		if is_minus_one(s) and not one_letter(s):
			if can_ijk(s):
				sol += "Case #" + str(ic+1) + ": YES\n"
			else:
				sol += "Case #" + str(ic+1) + ": NO\n"
		else:
			sol += "Case #" + str(ic+1) + ": NO\n"

	out_file = open(sys.argv[1]+"_sol", 'w')
	out_file.write(sol)