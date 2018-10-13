def bot_trust(file_in, file_out):
	file_in = open(file_in, "r")
	instructions = file_in.read()
	out = ""
	instructions = instructions.split("\n")
	for case in range(1, int(instructions.pop(0))+1, 1):
		both_orders = instructions.pop(0).split(" ")
		O_orders, B_orders, sequence = [], [], []
		order = 0
		del both_orders[0]
		for i in range(0, len(both_orders), 2):
			if both_orders[i] == "O":
				O_orders.append(int(both_orders[i+1]))
			elif both_orders[i] == "B":
				B_orders.append(int(both_orders[i+1]))
			order += 1
			sequence.append(both_orders[i])
		print "both:", both_orders
		print "O:", O_orders
		print "B:", B_orders
		print "sequence:", sequence
		# By now I have where each robot needs to go and the order in which 
		# they need to press the buttons
		end = False
		i, j = 0, 0
		O_pos, B_pos = 1, 1
		O_order, B_order = 0, 0
		print "Time | Orange           | Blue"
		print "-----+------------------+-----------------"
		while end == False:
			pushed = False
			try:
				if O_pos < O_orders[O_order]: 
					O_pos += 1
					so = "Move to button " + str(O_pos)
				elif O_pos > O_orders[O_order]: 
					O_pos -= 1
					so = "Move to button " + str(O_pos)
				elif sequence[j] == "O" and pushed == False:
					j+=1
					O_order +=1
					pushed = True
					so = "Push button " + str(O_pos) + "   "
				else: so = "Stay at button " + str(O_pos)
			except:pass
			try:
				if B_pos < B_orders[B_order]: 
					B_pos += 1
					sb = "Move to button " + str(B_pos)
				elif B_pos > B_orders[B_order]: 
					B_pos -= 1
					sb = "Move to button " + str(B_pos)
				elif sequence[j] == "B" and pushed == False:
					j+=1
					B_order+= 1
					pushed = True
					sb = "Push button " + str(B_pos) + "   "
				else: sb = "Stay at button " + str(B_pos)
			except:pass
			i += 1
			if j+1 > len(sequence): end = True 
			print "  %i  | %s | %s " % (i, so, sb)
		out+= "Case #"+ str(case) + ": " + str(i) + "\n"
	print out
	open(file_out, "w").write(out)
bot_trust("../downloads/A-large.in", "../downloads/A-large.out")
