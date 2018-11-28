import random 

def quicksort(L):
	if len(L) > 1:
		pivot = random.randrange(len(L))
		elements = L[:pivot]+L[pivot+1:]
		left  = [element for element in elements if element < L[pivot]] 
		right =[element for element in elements if element >= L[pivot]]
		return quicksort(left)+[L[pivot]]+quicksort(right)
	return L




fileIn = open("D-large.in", "r")
fileOut = open("output.in", "w")



loop = fileIn.readline().split()
#print loop[0], type(int(loop[0]))

for i in range(0, int(loop[0]) ):
	number = fileIn.readline().split()
	naomi = fileIn.readline().split()
	ken = fileIn.readline().split()	

	for j in range(0, int(number[0]) ):
		naomi[j] = float(naomi[j])
		ken[j] = float(ken[j])

	#print(naomi)
	#print(ken, end="\n")

	naomi = quicksort(naomi)
	ken = quicksort(ken)

	#print("sorted")
	#print(naomi)
	#print(ken, end="\n")


	#Optimal Deceitful War works by
	naomi2 = list(naomi)
	ken2 = list(ken)
	counterDeceit = 0;

	#print("len(ken2)", len(ken2))

	for j in reversed( range(0, len(ken2)) ):
		for k in reversed( range(0, len(naomi2)) ):
			if( ken2[j] <  naomi2[k]):		
				#print(naomi2[k],ken2[j])
				counterDeceit += 1	
				del ken2[j]
				del naomi2[k]
				break


	#Optimal War works by
 	#if max(naomi) > max(ken), pair max(naomi) and min(ken), counter++
	#else pair max(naomi) and max(ken)
	counterNormal = 0


	#print("len(ken)", len(ken))

	for j in reversed( range(0, len(naomi)) ):

		#print(ken[len(ken) - 1],  naomi[j])

		if( ken[len(ken) - 1] <  naomi[j] ):		
			#print("  ", naomi[j], ken[0], "+1")
			counterNormal += 1	
			del ken[0]
			del naomi[j]
		else:
			lowest = len(ken) - 1
			while( ken[lowest] >  naomi[j]):
				if(lowest != 0 and ken[lowest - 1] >  naomi[j]):
					lowest = lowest - 1
				else:
					break

			#print("  ", naomi[j], ken[lowest])
			del ken[lowest]
			del naomi[j]			

	#print("Deceitful War: ", counterDeceit, " Normal War: ", counterNormal, end="\n\n")
	fileOut.write( "Case #" + str(i + 1) + ": " + str(counterDeceit) + " " + str(counterNormal) + "\n");

fileIn.close()
fileOut.close()
