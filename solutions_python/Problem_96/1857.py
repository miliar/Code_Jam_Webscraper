Opened = open('B-small-attempt7.in', 'r')
Number = Opened.readline()
File = Opened.readlines()
Blank = []
Answers = []
Remove = []
Storage = []
Unique = []
Done = []
Awesome = []
Sup = []
for i in File:
	Stuff = i[:-1]
	Awesome.append(Stuff.split(" "))
	#print Awesome
	for x in Awesome:
		for j in x:
			Blank.append(j)
	#print Blank
	Numbers = []
	for z in Blank:
		try:
			Numbers.append(int(z))
		except ValueError:
			pass
	#print Numbers
	S = Numbers[1]
	P = Numbers[2]
	range = len(Numbers)
	NumF = Numbers[3:range]
	NumF.sort()
	#print NumF
	DC = []
	Unique = []
	Done = []
	
	#print S
	for y in NumF:
		if y == 0:
			List = [0,0,0]
			for i in List:
				if i >= P:
					Unique.append([0,0,0])
					break
		if y == 1:
			List = [0,0,1]
			for i in List:
				if i >= P:
					Unique.append([0,0,1])
					break
		if y == 2:
			if S > 0:
				List = [0,0,2]
				h = 0
				for i in List:
					if i >= P:
						Unique.append(List)
						S -= 1
						if S < 0:
							List = [0,0,1]
							for i in List:
								if i >= P:
									Unique.append([0,0,1])
									break
						break
					if h == 3: 
						List = [0,0,1]
						for i in List:
							if i >= P:
								Unique.append([0,0,1])
								break
					h += 1
			else:
				List = [0,0,1]
				for i in List:
					if i >= P:
						Unique.append([0,0,1])
						break

		if y == 3:
			if S > 0:
				List = [0,2,1]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([0,2,1])
						S -= 1
						if S < 0:
							List = [1,1,1]
							for i in List:
								if i >= P:
									Unique.append([1,1,1])
									break
						break
					if h == 3: 
						List = [1,1,1]
						for i in List:
							if i >= P:
								Unique.append([1,1,1])
								break
					h += 1
			else:
				List = [1,1,1]
				for i in List:
					if i >= P:
						Unique.append([1,1,1])
						break

		if y == 4:
			if S > 0:
				List = [0,2,2]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([0,2,2])
						S -= 1
						if S < 0:
							List = [1,1,2]
							for i in List:
								if i >= P:
									Unique.append([1,1,2])
									break
						break
					if h == 3:
						List = [1,1,2]
						for i in List:
							if i >= P:
								Unique.append([1,1,2])
								break
					h += 1
			else:
				List = [1,1,2]
				for i in List:
					if i >= P:
						Unique.append([1,1,2])
						break

			
		if y == 5:
			if S > 0:
				List = [1,1,3]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([1,1,3])
						S -= 1
						if S < 0:
							List = [2,2,1]
							for i in List:
								if i >= P:
									Unique.append([2,2,1])
									break
						break
					if h == 3:
						List = [2,2,1]
						for i in List:
							if i >= P:
								Unique.append([2,2,1])
								break
					h += 1
			else:
				List = [2,2,1]
				for i in List:
					if i >= P:
						Unique.append([2,2,1])
						break

		
		if y == 6:
			if S > 0:
				List = [1,2,3]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([1,2,3])
						S -= 1
						if S < 0:
							List = [2,2,2]
							for i in List:
								if i >= P:
									Unique.append([2,2,2])
									break
						break
					if h == 3:
						List = [2,2,2]
						for i in List:
							if i >= P:
								Unique.append([2,2,2])
								break
					h += 1
			else:
				List = [2,2,2]
				for i in List:
					if i >= P:
						Unique.append([2,2,2])
						break
			
		if y == 7:
			if S > 0:
				List = [3,3,1]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([3,3,1])
						S -= 1
						if S < 0:
							List = [2,2,3]
							for i in List:
								if i >= P:
									Unique.append([2,2,3])
									break
						break
					if h == 3: 
						List = [2,2,3]
						for i in List:
							if i >= P:
								Unique.append([2,2,3])
								break
					h += 1
			else:
				List = [2,2,3]
				for i in List:
					if i >= P:
						Unique.append([2,2,3])
						break

		if y == 8:
			if S > 0:
				List = [2,2,4]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([2,2,4])
						S -= 1
						if S < 0:
							List = [3,3,2]
							for i in List:
								if i >= P:
									Unique.append([3,3,2])
									break
						break
					if h == 3: 
						List = [3,3,2]
						for i in List:
							if i >= P:
								Unique.append([3,3,2])
								break
					h += 1
			else:
				List = [3,3,2]
				for i in List:
					if i >= P:
						Unique.append([3,3,2])
						break

		if y == 9:
			if S > 0:
				List = [2,3,4]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([2,3,4])
						S -= 1
						if S < 0:
							List = [3,3,3]
							for i in List:
								if i >= P:
									Unique.append([3,3,3])
									break
						break
					if h == 3:
						List = [3,3,3]
						for i in List:
							if i >= P:
								Unique.append([3,3,3])
								break
					h += 1
			else:
				List = [3,3,3]
				for i in List:
					if i >= P:
						Unique.append([3,3,3])
						break
		if y == 10:
			if S > 0:
				List = [4,4,2]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([4,4,2])
						S -= 1
						if S < 0:
							List = [3,3,4]
							for i in List:
								if i >= P:
									Unique.append([3,3,4])
									break
						break
					if h == 3:
						List = [3,3,4]
						for i in List:
							if i >= P:
								Unique.append([3,3,4])
								break
					h += 1
			else:
				List = [3,3,4]
				for i in List:
					if i >= P:
						Unique.append([3,3,4])
						break

		if y == 11:
			if S > 0:
				List = [3,3,5]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([3,3,5])
						S -= 1
						if S < 0:
							List = [4,4,3]
							for i in List:
								if i >= P:
									Unique.append([4,4,3])
									break
						break
					if h == 3: 
						List = [4,4,3]
						for i in List:
							if i >= P:
								Unique.append([4,4,3])
								break
					h += 1
			else:
				List = [4,4,3]
				for i in List:
					if i >= P:
						Unique.append([4,4,3])
						break
		if y == 12:
			if S > 0:
				List = [3,4,5]
				h = 0
				for i in List:
					if i >= P:
						Unique.append(List)
						S -= 1
						if S < 0:
							List = [4,4,4]
							for i in List:
								if i >= P:
									Unique.append([4,4,4])
									break
						break
					if h == 3:
						List = [4,4,4]
						for i in List:
							if i >= P:
								Unique.append([4,4,4])
								break
					h += 1
			
			else:
				List = [4,4,4]
				for i in List:
					if i >= P:
						Unique.append([4,4,4])
						break
		if y == 13:
			if S > 0:
				List = [5,5,3]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([5,5,3])
						S -= 1
						if S < 0:
							List = [4,4,5]
							for i in List:
								if i >= P:
									Unique.append([4,4,5])
									break
						break
					if h == 3:
						List = [4,4,5]
						for i in List:
							if i >= P:
								Unique.append([4,4,5])
								break
					h += 1
			else:
				List = [4,4,5]
				for i in List:
					if i >= P:
						Unique.append([4,4,5])
						break

		if y == 14:
			if S > 0:
				List = [4,4,6]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([4,4,6])
						S -= 1
						if S < 0:
							List = [5,5,4]
							for i in List:
								if i >= P:
									Unique.append([5,5,4])
									break
						break
					if h == 3:
						List = [5,5,4]
						for i in List:
							if i >= P:
								Unique.append([5,5,4])
								break
					h += 1
			else:
				List = [5,5,4]
				for i in List:
					if i >= P:
						Unique.append([5,5,4])
						break

		if y == 15:
			if S > 0:
				List = [4,5,6]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([4,5,6])
						S -= 1
						if S < 0:
							List = [5,5,5]
							for i in List:
								if i >= P:
									Unique.append([5,5,5])
									break
						break
					if h == 3:
						List = [5,5,5]
						for i in List:
							if i >= P:
								Unique.append([5,5,5])
								break
					h += 1
			else:
				List = [5,5,5]
				for i in List:
					if i >= P:
						Unique.append([5,5,5])
						break
		if y == 16:
			if S > 0:
				List = [6,6,4]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([6,6,4])
						S -= 1
						if S < 0:
							List = [5,5,6]
							for i in List:
								if i >= P:
									Unique.append([5,5,6])
									break
						break
					if h == 3:
						List = [5,5,6]
						for i in List:
							if i >= P:
								Unique.append([5,5,6])
								break
					h += 1
			else:
				List = [5,5,6]
				for i in List:
					if i >= P:
						Unique.append([5,5,6])
						break

		if y == 17:
			if S > 0:
				List = [5,5,7]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([5,5,7])
						S -= 1
						if S < 0:
							List = [6,6,5]
							for i in List:
								if i >= P:
									Unique.append([6,6,5])
									break
						break
					if h == 3:
						List = [6,6,5]
						for i in List:
							if i >= P:
								Unique.append([6,6,5])
								break
					h += 1
			else:
				List = [6,6,5]
				for i in List:
					if i >= P:
						Unique.append([6,6,5])
						break

		if y == 18:
			if S > 0:
				List = [5,6,7]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([5,6,7])
						S -= 1
						if S < 0:
							List = [6,6,6]
							for i in List:
								if i >= P:
									Unique.append([6,6,6])
									break
						break
					if h == 3:
						List = [6,6,6]
						for i in List:
							if i >= P:
								Unique.append([6,6,6])
								break
					h += 1
			else:
				List = [6,6,6]
				for i in List:
					if i >= P:
						Unique.append([6,6,6])
						break
		if y == 19:
			if S > 0:
				List = [7,7,5]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([7,7,5])
						S -= 1
						if S < 0:
							List = [6,6,7]
							for i in List:
								if i >= P:
									Unique.append([6,6,7])
									break
						break
					if h == 3:
						List = [6,6,7]
						for i in List:
							if i >= P:
								Unique.append([6,6,7])
								break
					h += 1
			else:
				List = [6,6,7]
				for i in List:
					if i >= P:
						Unique.append([6,6,7])
						break

		if y == 20:
			if S > 0:
				List = [6,6,8]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([6,6,8])
						S -= 1
						if S < 0:
							List = [7,7,6]
							for i in List:
								if i >= P:
									Unique.append([7,7,6])
									break
						break
					if h == 3:
						List = [7,7,6]
						for i in List:
							if i >= P:
								Unique.append([7,7,6])
								break
					h += 1
			else:
				List = [7,7,6]
				for i in List:
					if i >= P:
						Unique.append([7,7,6])
						break

		if y == 21:
			if S > 0:
				List = [6,7,8]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([6,7,8])
						S -= 1
						if S < 0:
							List = [7,7,7]
							for i in List:
								if i >= P:
									Unique.append([7,7,7])
									break
						break
					if h == 3:
						List = [7,7,7]
						for i in List:
							if i >= P:
								Unique.append([7,7,7])
								break
					h += 1
			else:
				List = [7,7,7]
				for i in List:
					if i >= P:
						Unique.append([7,7,7])
						break
		if y == 22:
			if S > 0:
				List = [8,8,6]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([8,8,6])
						S -= 1
						if S < 0:
							List = [7,7,8]
							for i in List:
								if i >= P:
									Unique.append([7,7,8])
									break
						break
					if h == 3:
						List = [7,7,8]
						for i in List:
							if i >= P:
								Unique.append([7,7,8])
								break
					h += 1
			else:
				List = [7,7,8]
				for i in List:
					if i >= P:
						Unique.append([7,7,8])
						break

		if y == 23:
			if S > 0:
				List = [7,7,9]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([7,7,9])
						S -= 1
						if S < 0:
							List = [8,8,7]
							for i in List:
								if i >= P:
									Unique.append([8,8,7])
									break
						break
					if h == 3:
						List = [8,8,7]
						for i in List:
							if i >= P:
								Unique.append([8,8,7])
								break
					h += 1
			else:
				List = [8,8,7]
				for i in List:
					if i >= P:
						Unique.append([8,8,7])
						break

		if y == 24:
			if S > 0:
				List = [7,8,9]
				h = 0
				for i in List:
					if i >= P:
						Unique.append(List)
						S -= 1
						if S < 0:
							List = [8,8,8]
							for i in List:
								if i >= P:
									Unique.append([8,8,8])
									break
						break
					if h == 3:
						List = [8,8,8]
						for i in List:
							if i >= P:
								Unique.append([8,8,8])
								break
					h += 1
			else:
				List = [8,8,8]
				for i in List:
					if i >= P:
						Unique.append([8,8,8])
						break
		if y == 25:
			if S > 0:
				List = [9,9,7]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([9,9,7])
						S -= 1
						if S < 0:
							List = [8,8,9]
							for i in List:
								if i >= P:
									Unique.append([8,8,9])
									break
						break
					if h == 3:
						List = [8,8,9]
						for i in List:
							if i >= P:
								Unique.append([8,8,9])
								break
					h += 1
			else:
				List = [8,8,9]
				for i in List:
					if i >= P:
						Unique.append([8,8,9])
						break

		if y == 26:
			if S > 0:
				List = [8,8,10]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([8,8,10])
						S -= 1
						if S < 0:
							List = [9,9,8]
							for i in List:
								if i >= P:
									Unique.append([9,9,8])
									break
						break
					if h == 3:
						List = [9,9,8]
						for i in List:
							if i >= P:
								Unique.append([9,9,8])
								break
					h += 1
			else:
				List = [9,9,8]
				for i in List:
					if i >= P:
						Unique.append([9,9,8])
						break

		if y == 27:
			if S > 0:
				List = [8,9,10]
				h = 0
				for i in List:
					if i >= P:
						Unique.append(List)
						S -= 1
						if S < 0:
							List = [9,9,9]
							for i in List:
								if i >= P:
									Unique.append([9,9,9])
									break
						break
					if h == 3:
						List = [9,9,9]
						for i in List:
							if i >= P:
								Unique.append([9,9,9])
								break
					h += 1
			else:
				List = [9,9,9]
				for i in List:
					if i >= P:
						Unique.append([9,9,9])
						break
		if y == 28:
			if S > 0:
				List = [10,10,8]
				h = 0
				for i in List:
					if i >= P:
						Unique.append([10,10,8])
						S -= 1
						if S < 0:
							List = [9,9,10]
							for i in List:
								if i >= P:
									Unique.append([9,9,10])
									break
						break
					if h == 3:
						List = [9,9,10]
						for i in List:
							if i >= P:
								Unique.append([9,9,10])
								break
					h += 1
			else:
				List = [9,9,10]
				for i in List:
					if i >= P:
						Unique.append([9,9,10])
						break

		if y == 29:
			List = [10,10,9]
			for i in List:
				if i >= P:
					Unique.append([10,10,9])
					break
		if y == 30:
			List = [10,10,10]
			for i in List:
				if i >= P:
					Unique.append([10,10,10])
					break
		#print Unique
		#print Unique
			
#	if S > 0:
	#for i in Unique:
	#	for X in i:
	#		q = 0
	#		if X >= P:
	#			Remove.append(i)
	#			Answers.append(X)
				
#			i.remove(i[q])
	#		q += 1
	#for i in Unique:
	#	for X in i:
	#		r = 0
	#		if X >= P:
	#			Remove.append(i)
	#			Answers.append(X)
				
#			#i.remove(i[r])
	#		r += 1
				
	#for i in Unique:
	#	if i not in Done:
	#		Done.append(i)
	#for i in Sup:
	#	if i not in Done:
	#		Done.append(len(i))

	#print Remove
	
	
	#print Unique
	Storage.append(len(Unique))
	Unique = []
	Done = []
	Answers = []
	Blank = []
	Awesome = []
#print File
#print Number
#print Remove
#print Answers



z = 1
for i in Storage:
	print 'Case #'+str(z)+': '+str(i)
	z += 1