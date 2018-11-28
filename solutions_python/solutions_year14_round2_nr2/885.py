def maquina():
	file_name = "input.txt"
	objecto_archivo = open(file_name, 'r')
	count_case = int(objecto_archivo.readline()[:-1])
	for number_case in range(0, count_case): 
		frase = "Case #"+str(number_case +1)+": "
		values =  objecto_archivo.readline()[:-1]
		A,B,K = values.split(" ")
		count_result = count_of_result(int(A), int(B), int(K))
		frase += str(count_result)
		print frase
	objecto_archivo.close()

def count_of_result(a_lala, b_lala, k_lala):
	#import ipdb,pprint; ipdb.set_trace()
	result = 0
	for i_index in range(0,a_lala):
		for j_index in range (0, b_lala):
			if ( i_index & j_index ) < k_lala:
				result+=1
			

	
	return result

if __name__ == "__main__":
	maquina()