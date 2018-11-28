#!/usr/bin/python
import sys


def search_inv_ind(ind, cstr, dstr, nstr):
	j=ind
	result = ''
	#clr_flg = False
	#clr_text = ''
	#clr_flg_pos = 0
	while j<len(nstr):
		chg_flg = 0
		if nstr[j] == cstr[0]  or nstr[j] == cstr[1]:
			if len(result)>0:
				if result[-1] == (cstr[0] if nstr[j]==cstr[1] else cstr[1]):
					chg_flg = 2
				else:
					chg_flg = 1
			else:
				chg_flg = 1
		
		if chg_flg == 2:
			#if clr_flg and clr_flg_pos==j-1:
			#	if nstr[j-1] != cstr[2]:
			#		clr_flg = False
			result = result[0:len(result)-1]
			result += cstr[2]
			
		elif nstr[j] == dstr[0] or nstr[j] == dstr[1]:
			if (dstr[0] if nstr[j]==dstr[1] else dstr[1]) in result:
				result = ''
			else:
				result += nstr[j]
				
			"""
			if clr_flg:
				if clr_text == nstr[j]:
					result = ''
					clr_flg = False
				else:
					print 'hoge'
					clr_flg = True
					clr_flg_pos = j
					clr_text = dstr[0] if nstr[j]==dstr[1] else dstr[1]
					result += nstr[j]
			else:
				clr_flg = True
				clr_flg_pos = j
				clr_text = dstr[0] if nstr[j]==dstr[1] else dstr[1]
				result += nstr[j]
			"""
		else:
			result += nstr[j]
		j += 1
	return result

if len(sys.argv) == 3:
	lines = open(sys.argv[1], 'r').readlines()
	fw = open(sys.argv[2], 'w')
else:
	sys.exit('Usage: %s in_filename out_filename' % sys.argv[0])


"""
lines = ['5'
,'0 0 2 EA'
,'1 QRI 0 4 RRQR'
,'1 QFT 1 QF 7 FAQFDFQ'
,'1 EEZ 1 QE 7 QEEEERA'
,'0 1 QW 2 QW']
"""

numofcases = int(lines[0])
cursor = 1
for i in range(0, numofcases):
	
	param = lines[cursor].replace('\n','').split(' ')
	cursor += 1
	
	intc = int(param[0])
	if intc>0:
		cstr = param[1]
		intd = int(param[2])
		if intd>0:
			dstr = param[3]
			N = int(param[4])
			nstr = param[5]
		else:
			dstr = '--'
			N = int(param[3])
			nstr = param[4]
	else:
		cstr = '---'
		intd = int(param[1])
		if intd>0:
			dstr = param[2]
			N = int(param[3])
			nstr = param[4]
		else:
			dstr = '--'
			N = param[2]
			nstr = param[3]
	
	#print intc, cstr, intd, dstr, N, nstr
	
	result = search_inv_ind(0, cstr, dstr, nstr)
	result = list(result)
	result = str(result).replace("'","")
	print 'Case #' + str(i+1) + ': ' + str(result)
	fw.write('Case #' + str(i+1) + ': ' + result + '\n')

fw.close()

