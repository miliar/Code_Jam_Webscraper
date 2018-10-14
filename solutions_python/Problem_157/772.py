'''
Created on Apr 11, 2015

@author: Ankur Patil
'''
import sys
def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		table = {
					("i","1"):"i",
					("i","i"):"-1",
					("i","j"):"k",
					("i","k"):"-j",
					("j","1"):"j",
					("j","i"):"-k",
					("j","j"):"-1",
					("j","k"):"i",
					("k","1"):"k",
					("k","i"):"j",
					("k","j"):"-i",
					("k","k"):"-1",
					("1","1"):"1",
					("1","i"):"i",
					("1","j"):"j",
					("1","k"):"k",
				}
		for t in range(1,T+1):
			tokens = f.readline().split()
			L = int(tokens[0])
			X = int(tokens[1])
			str = f.readline()[:L]
			cnt = 0
			is_negative = False
			if(False):
				new_cnt = str.count("ii") + str.count("jj") + str.count("kk")
				#if new_cnt == 0: break
				is_negative = new_cnt % 2
				str = str.replace("ii","").replace("jj","").replace("kk","")
			req = ["i","j","k"]
			#print(str)
			if is_negative:
				curr = "-1"
			else:
				curr = "1"
			flag = False
			for i in range(X):
				for c in str:
					if curr == req[0]:
						if len(req) == 1:
							req[0] = "1"
						else:
							req = req[1:]
						curr = "1"
					if curr[0] == "-":
						is_negative = True
						curr = curr[1:]
					else:
						is_negative = False
					key = (curr,c)
					if is_negative:
						if table[key][0] != "-":
							curr = "-"+table[key]
						else:
							curr = table[key][1:]
					else:
						curr = table[key]
			else:
				flag = True
			if flag == True and req[0] == curr:
				ans = "YES"
			else:
				ans = "NO"
			sol.append("Case #{0}: {1}\n".format(t,ans))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])