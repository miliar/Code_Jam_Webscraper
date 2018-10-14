def calc(l, o = '+'):
	"""
		calc([1,2,3,4],o) -> 1o2o3o4 -> 1+2+3+4 = 10
	"""
	return eval(o.join([str(c) for c in l]))

def base2(N):
	"""
		equivale:
			math.pow(2,N)-1
			int(calc([2 for x in range(0,N)],'*')-1)
	"""
	return int(eval('*'.join([str(2) for x in range(0,N)]))-1)

class dotest:
	"""
		obj = dotest('arquivo-de-entrada')
		obj.y('Result') -> Case #x: Result
		o valor x eh auto incrementado
		
		o __init__ cria
		
		self.fout = instancia o arquivo de saida
		self.fo = funcao de escriva no arquivo de saida
		self.fi = linhas do arquivo
		self.T = Total de casos
		
	"""
	def __init__(self, fname):
		self.x = 0
		self.lastY = None
		fin = open('%s.in' % fname, 'r')
		fi = [l.strip() for l in fin.readlines()]
		fin.close()
		fout = open('%s.out' % fname, 'w')
		self.fout, self.fo, self.fi, self.T = fout, self.y, fi, range(1,int(fi.pop(0))+1)

	def y(self, y):
		self.x += 1
		self.lastY = y
		self.fout.write('Case #%d: %s\n' % (self.x, str(y)))
		return self.x

if __name__ == '__main__':		
	test =  dotest('A-large-practice')
	test.y('1')
	test.y('asd')
	print base2(3)