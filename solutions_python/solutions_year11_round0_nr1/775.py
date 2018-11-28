#coding:utf-8
import sys,time

class State:
	def __init__(self,pos,goal):
		self.pos = pos
		self.goal = goal
		

def do_one_case(fin):
	ans = ("")
	P = fin.readline().split()
	N = P[0]
#	print N
#	print P
	Q = P[1::2]
	lst = P[1::2]
	lstnum =map(int, P[2::2])
#	print lst
#	print lstnum
	sec = 0
	if "O" in lst:
		orange = State(1,lstnum.pop(lst.index("O")))
		lst.remove("O")
	else:
		orange = State(1,1)
	if "B" in lst:
		blue = State(1,lstnum.pop(lst.index("B")))
		lst.remove("B")
	else:
		blue = State(1,1)
	current = Q.pop(0)
#	print orange.goal,blue.goal,current,lst
	#exit()
	

#	print "start!!"
	while True:
		sec += 1
		tmp = ""
#		print Q
#		print sec,current,"orange",orange.pos,orange.goal,"blue",blue.pos,blue.goal
#		print current == "O"
#		time.sleep(0.5)
		if current == "O" and orange.goal == orange.pos: #目標に辿り着いていれば
			if len(Q) == 0:
				break
#			print "O,pop",Q
			tmp = Q.pop(0)
			if "O" in lst: #次の目標があれば
				orange.goal = lstnum.pop(lst.index("O"))
				lst.remove("O")
		else: #辿り着いていなければ
			if orange.goal > orange.pos:
				orange.pos += 1
			elif orange.goal < orange.pos:
				orange.pos -= 1
				
		if current == "B" and blue.goal == blue.pos:
			if len(Q) == 0:
				break
			tmp = Q.pop(0)
#			print "B,pop",Q
			if "B" in lst:
				blue.goal = lstnum.pop(lst.index("B"))
				lst.remove("B")
		else:
			if blue.goal > blue.pos:
				blue.pos+= 1
			elif blue.goal < blue.pos:
				blue.pos -= 1
		if not tmp == "":
			current = tmp
		
	return str(sec)


def main(fin,fout):
	N = int(fin.readline())
	for i in xrange(N):
		result = "Case #"+str(i+1)+": "+do_one_case(fin)
		print result
		fout.write(result+"\n")


if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		fin = open(sys.argv[1].upper() + "-small-attempt0 (1).in")
	elif len(sys.argv) == 3:
		if sys.argv[1] == sys.argv[2]: #誤入力防止
			fin = open(sys.argv[1].upper() + "-large.in")
	else:
		fin = open("zinput.txt")
	fout = open("zoutput.txt","w")
	main(fin,fout)
	fin.close()
	fin.close()
#	main(sys.stdin)

