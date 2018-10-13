



def mago():
	file_name = "inputs"
	objecto_archivo = open(file_name, 'r')
	count_case = int(objecto_archivo.readline()[:-1])
	
	for number_case in range(0, count_case): 
		frase = "Case #"+str(number_case +1)+": "
		first_result = []
		second_result = []
		final_result =[]
		values =  int(objecto_archivo.readline()[:-1])
		for horizontal_line in range(1, 5):
			result = objecto_archivo.readline()[:-1]
			if horizontal_line is values:
				first_result=result.split(" ")		
		values = int(objecto_archivo.readline()[:-1])
		for vertical_line in range(1, 5):
			result = objecto_archivo.readline()[:-1]
			if vertical_line is values:
				second_result=result.split(" ")
		for num in first_result:
			if num in second_result:
				final_result.append(num)
		
		result_print(final_result, frase)

	objecto_archivo.close()


def result_print(array_final_result, frase):
	tamano_array = len(array_final_result)
	if tamano_array == 1: 
		print frase+array_final_result[0]
	if tamano_array > 1:
		print frase+"Bad magician!"
	if tamano_array == 0:
		print frase+"Volunteer cheated!"

if __name__ == "__main__":
	mago()