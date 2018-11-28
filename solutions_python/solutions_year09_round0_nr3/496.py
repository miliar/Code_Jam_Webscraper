import os, math
FILENAME = "C-small-attempt0."

#get input
def clean_read(inpf):
	list = ((inpf.readline()).strip('\n ')).split(' ')
	if len(list) == 1:
		return list[0]
	return list

inpf = open(FILENAME + "in", 'r')
case_cnt = int(clean_read(inpf))
input = []
for i in range(case_cnt):
	phrase = clean_read(inpf)
	dddd=[]
	for j in range(len(phrase)):
		if len(dddd):
			dddd.append(' ')
		for k in range(len(phrase[j])):
			dddd.append(phrase[j][k])
	input.append(dddd)
inpf.close()

'''
#solution
def tail_rec(fun):
	def tail(fun):
		a = fun
		while callable(a):
			a = a()
		return a
	return (lambda x, y: tail(fun(x, y)))
'''

def find_substring(main, sub):
	if sub and len(sub) > 0:
		if len(main) > 0:
			sum = 0
			for i in range(len(main)):
				if sub[0] == main[i]:
					n = i+1
					#t = (lambda: find_substring(main[n:], sub[1:]))
					t = find_substring(main[n:], sub[1:])
					sum += t
				else:
					continue
			return sum
		else:
			return 0
	else:
		return 1


#substringer = tail_rec(find_substring)
zz = 0
outf = open(FILENAME + "out", 'w')
input_string = ['w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m']
for strdud in input:
	ls = find_substring(strdud, input_string)
	ls += 1
	ls -= 1
	
	zz += 1
	if ls == 0:
		outf.write("Case #" + str(zz) + ": 0000\n")
	elif ls < 10:
		outf.write("Case #" + str(zz) + ": 000" + str(ls) + "\n")
	elif ls < 100:
		outf.write("Case #" + str(zz) + ": 00" + str(ls) + "\n")
	elif ls < 1000:
		outf.write("Case #" + str(zz) + ": 0" + str(ls) + "\n")
	else:
		dude = int(ls / 1000)
		ls -= 1000*dude
		outf.write("Case #" + str(zz) + ": " + str(ls) + "\n")

outf.close()
