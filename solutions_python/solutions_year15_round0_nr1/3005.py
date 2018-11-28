import sys

def main():
	f = open('inp1.in','r')
	all_lines = f.readlines()
	n = int(all_lines[0])
	op = open('op.txt','w')
	for ite in range(1,n+1):
		cur_line = all_lines[ite]
		max_shy,ppl_shy = cur_line.split(' ')[0], cur_line.split(' ')[1]
		ppl_req = 0
		tot_ppl = 0
		ite1 = 0
		ppl_shy = ppl_shy.strip()
		for i in str(ppl_shy):
			if tot_ppl < ite1:
				ppl_req = ppl_req + 1
				tot_ppl = tot_ppl + 1
			tot_ppl = tot_ppl + int(i)
			ite1 = ite1 + 1
		op_line = 'Case #'+str(ite)+': '+str(ppl_req)+'\n'
		op.write(op_line)

if __name__ == '__main__':
	main()