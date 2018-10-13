import io
def do_case(case_num, board):
	result = "x"# decide(board)
	print "Case #%d: %s" % (case_num, result)

def main():
	fname="A-small-attempt1.in"
	T=0#test cases
	with open(fname) as f:
		content = f.readlines()
		T=first=int(content.pop(0))
		case=0
		for line in content:
			line = line.strip()
			stream = io.TextIOWrapper(io.BytesIO(line))
			max_shy=int(stream.read(1))
			stream.read(1)#ignore whitespace
			shy_map=[]
			for x in range(0,max_shy+1):
				shy_map.append(int(stream.read(1)))
			#wszystko wczytane
			added=0
			count=0
			for x in range(0,max_shy+1):
				#print ""
				if x>count and shy_map[x]>0:#brakuje nam owacji
					added += x-count
					count += added
				count += shy_map[x]
			print "Case #%d: %d" % (case+1,added)
			case += 1

if __name__ == "__main__":
	main()
	