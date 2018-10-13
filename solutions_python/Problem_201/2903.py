file_3 = open("Outputs.txt","w")

def solution(n,k,count_1):

	list1 = [0 for h in xrange(n+2)]

	diagram = ["." for an in xrange(n+2)]

	left = [0 for v in xrange(n+2)]

	right = [0 for x in xrange(n+2)]

	list1[0] = 1

	length = len(list1)

	list1[length-1] = 1

	diagram[0] = "O"

	diagram[len(diagram)-1]="O"


	ans = []
	choosen_indexes = []
	choosen_indexes.append(0)
	choosen_indexes.append(n+1)

	def qwerty(choosen):


		diagram[choosen]="O"		

		left[choosen] = -2

		right[choosen] = -2 

		

		leng = len(choosen_indexes)
		index_1=None
		index_2=None

		for u in xrange(leng-1):
			if choosen_indexes[u]<choosen  and choosen_indexes[u+1]>choosen:
				index_1 = choosen_indexes[u]
				index_2 = choosen_indexes[u+1]
				break

		# print index_1,index_2

		for a in xrange(index_1+1,choosen):
			right[a] = choosen-a-1

		for b in xrange(choosen+1,index_2):
			left[b] = b - choosen-1

		# print left,right
		# print "".join(str(j) for j in list1)

		choosen_indexes.append(choosen)
		choosen_indexes.sort()


	def start():
		for q in xrange(1,length-1):
			left[q] = q-1 
			right[q] = n-q


	start()
	# print left,right

	count = 0

	while count<k:
		choosen = n+8
		indexes_1 = []
		max_list = []
		indexes_2 = [] 	
		min_list = []

		for y in xrange(1,length-1):
			if left[y]>=0:
				if right[y]>=0:
					min_list.append(min(left[y],right[y]))

		var = max(min_list)

		for r in xrange(1,length-1):
			if min(left[r],right[r])==var:
				indexes_1.append(r)

		if len(indexes_1)>1:
			for index in indexes_1:
				max_list.append(max(left[index],right[index]))
			
			var_2 = max(max_list)

			for z in indexes_1:
				if var_2==max(left[z],right[z]):
					indexes_2.append(z)

			if len(indexes_2)>1:
				choosen = indexes_2[0]
			elif len(indexes_2)==1:
				choosen = indexes_2[0]

		elif len(indexes_1)==1:
			choosen = indexes_1[0]

		# print min_list
		# print max_list
		if count==k-1:
			ans.append(right[choosen])
			ans.append(left[choosen])
			file_3.write("Case #"+str(count_1)+": "+"".join(str(members)+" " for members in ans)+"\n")
			print "".join(str(members)+" " for members in ans)
		# print choosen,count,choosen in choosen_indexes
		qwerty(choosen)
		# print left
		# print right
		# print indexes_1
		# print indexes_2
		
		# print "".join(memb for memb in diagram)
		count+=1
		# print count
		# print "".join(str(members)+" " for members in ans)
	
	# print ans		

# solution(4,2)



# # solution(6,1)
# for obj in xrange(100):
# 	solution(1000,obj)
# 	print obj


def file_opener(filename):

	
	with open(filename,"r") as file_2:
		testcases = next(file_2)
		count = 1
		for line in file_2:
			line = line.strip()
			n,k = line.split()
			n,k = int(n),int(k)
			solution(n,k,count)
			# print "Case #"+str(count)+": "+str(n),str(k)
			count+=1
		file_2.close()

	
	

file_opener("C-small-1-attempt0.in")
file_3=open("Outputs.txt","r")
print file_3.read()
