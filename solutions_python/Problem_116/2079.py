def test(ip):
	arr = [[0 for x in xrange(4)] for x in xrange(4)]
	for row in range(0,4):
                input_list = ip.pop(0)
		for coloumn in range(0,4):
			arr[row][coloumn] = input_list[coloumn]
        j = ip.pop(0)
        #print arr
	result = 0
	for row in range(0,4):    # just for the rows
		x, o = 0, 0
		for coloumn in range(0,4):
			if arr[row][coloumn]=='X':
				x = x + 1
			elif arr[row][coloumn]=='O':
				o = o + 1
                #print "Rows: x= " + str(x) + " o= " + str(o)
		result, cmd = decision(x, o, arr[row])
                if cmd != None:
                   return cmd
       
        for coloumn in range(0,4):    # just for the coloumn
		x, o = 0, 0
                li = []
		for row in range(0,4):
                        li.append(arr[row][coloumn])
			if arr[row][coloumn]=='X':
				x = x + 1
			elif arr[row][coloumn]=='O':
				o = o + 1
                #print li, x, o
		result, cmd = decision(x, o, li)
                if cmd != None:
                   return cmd
               
        li = []
        x, o = 0, 0
	for e in range(0,4):     #just for the 0 diognal
                li.append(arr[e][e])
                if arr[e][e]=='X':
				x = x + 1
		elif arr[e][e]=='O':
				o = o + 1
	result, cmd = decision(x, o, li)
        if cmd != None:
           return cmd

        li = []
        x, o = 0, 0
        for e in range(3,-1,-1):     #just for the opposite diognal
                #print arr[3-e][e]
                li.append(arr[3-e][e])
                if arr[3-e][e]=='X':
				x = x + 1
		elif arr[3-e][e]=='O':
				o = o + 1
	result, cmd = decision(x, o, li)
        if cmd != None:
           return cmd


	if result==0:
		for e in range(0,4):
			if "." in arr[e]:
				cmd =  "incomplete"
				result = 1
				break
		if result==0:
			cmd = "draw"

        return cmd


def decision(x, o, ch):
	for e in range(0,4):
		if x==4:
			cmd = "X"
                        return 1, cmd
			break
		elif o==4:
			cmd = "O"
                        return 1, cmd
			break
		if x==3 and 'T' in ch:
			cmd = "X"
                        return 1, cmd
			break
		elif o==3 and 'T' in ch:
			cmd = "O"
                        return 1, cmd
			break
                return 0, None

def read_ip():
	f = open("/home/neo/code_jam_2013/input", "r")
	li = f.readlines()
	f.close()
	for e in range(0,len(li)):
		li[e] = li[e].strip("\n")
	return li



def main():
	ip = read_ip()
	cases = int(ip.pop(0))
	for e in range(0,cases):
		re = test(ip)
		if re=="X":
			print "Case #" + str(e+1) + ": " + "X won"
		elif re=="O":
			print "Case #" + str(e+1) + ": " + "O won"
		elif re=="incomplete":
			print "Case #" + str(e+1) + ": " + "Game has not completed"
		elif re=="draw":
			print "Case #" + str(e+1) + ": " + "Draw"

if __name__=="__main__":
	main()
