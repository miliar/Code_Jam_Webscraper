def main():

	fr = open('input.in' , 'r')
	fw = open('output.out' , 'w')



	not_finish = False
	draw = False

	
	winy = False
	winx = False

	input_nr = 0
	row = col = 4
	arr = []

	string_data_row = ''
	string_data_col = ''

	NR_CASE=0;

	for line in    fr  :

		print "===== " + line
		

		if(input_nr == 0):
			input_nr = int(line)
			#print input_nr
		else:
			str_data = line.strip()
			str_dataO = str_data
			data_row = [c for c in str_data]
			# print str_data
			# print data_row




			if data_row!=[] and NR_CASE<input_nr:

				string_data_row += str_data

				str_data = str_data.replace('T', 'X')
				str_dataO = str_dataO.replace('T' , 'O')
				# print str_dataO

				if str_data == 'XXXX' :

					winx = True
					# print winx
				elif str_dataO == 'OOOO':
					winy = True

				arr.append(data_row)
				# print arr

			else:
				NR_CASE+=1

				print "aaaaaaaaaaaaa  " + str(winx)
				if winx :
					print 'dfdfdf'
					fw.write("Case #" + str(NR_CASE) + ": X won\n")
					# winx = False

				elif winy:
					fw.write("Case #" + str(NR_CASE) + ": O won\n")
					# winy = False

				
				else:

					# -----------------------VERTICALE----------------------------------------------
					strX =''
					strO =''
					for i in xrange(row):

						# winy = False
						# winx = False
						for j in xrange(col):
							strX += arr[j][i]
							strO += arr[j][i]
							print strX + "    " + strO

						# string_data_col += strX

						strX = strX.replace('T' , 'X')
						strO = strO.replace('T' , 'O')

						if strX == 'XXXX' :
							fw.write("Case #" + str(NR_CASE) + ": X won\n")
							winx = True
							# print winx
						elif strO == 'OOOO':
							fw.write("Case #" + str(NR_CASE) + ": O won\n")
							winy = True


						strX = ''
						strO = ''
					#----------------------------------------------------------------------
						
					if(not winx and not winy):

						diagonale1 = reduce(lambda x,y : x+y , [arr[i][i] for i in [0,1,2,3] ])
						diagonale2 = reduce(lambda x,y : x+y , [arr[3-i][i] for i in [3,2,1,0] ])

						# print "diagonale1   " + diagonale1
						# print "diagonale2   " + diagonale2

						diagonale1X = diagonale1.replace('T' , 'X')
						diagonale1O = diagonale1.replace('T' , 'O')

						if diagonale1X == 'XXXX' :
							fw.write("Case #" + str(NR_CASE) + ": X won\n")
							winx = True
							# print winx
						elif diagonale1O == 'OOOO':
							fw.write("Case #" + str(NR_CASE) + ": O won\n")
							winy = True

						diagonale2X = diagonale2.replace('T' , 'X')
						diagonale2O = diagonale2.replace('T' , 'O')

						if diagonale2X == 'XXXX' :
							fw.write("Case #" + str(NR_CASE) + ": X won\n")
							winx = True
							# print winx
						elif diagonale2O == 'OOOO':
							fw.write("Case #" + str(NR_CASE) + ": O won\n")
							winy = True


					# print winx
					# print winy
					if string_data_row.count('.') > 0 and (not winx and  not winy):
						print "not completed"
						fw.write("Case #"  + str(NR_CASE) + ": Game has not completed\n")

					elif not winx and  not winy :
						print "draw"
						fw.write("Case #" + str(NR_CASE) + ": Draw\n")


					# winx = False
					# winy = False


				arr = []
				string_data_row = ''

				winy = False
				winx = False


	fr.close()
	fw.close()


if __name__ == '__main__':
	main()

