import math

def opt(s_load,c_load):
	return max(max(c_load),max([int(math.ceil(sum(s_load[:(i+1)])/float(i+1))) for i in range(len(s_load))]))

fi = open("B-large.in.txt","r")
fo = open("output","w")
numinst = int(fi.readline())
for k in range(numinst):
	inst = fi.readline().split()
	seats = int(inst[0])
	customers = int(inst[1])
	tickets = int(inst[2])
	customers_tickets = [[] for _ in range(customers)]
	seats_tickets = [[] for _ in range(seats)]
	customers_load = [0 for _ in range(customers)]
	seats_load = [0 for _ in range(seats)]
	for j in range(tickets):
		ticket = fi.readline().split()	
		seats_tickets[int(ticket[0])-1] += [int(ticket[1])]
		customers_tickets[int(ticket[1])-1] += [int(ticket[0])]
		seats_load[int(ticket[0])-1] += 1
		customers_load[int(ticket[1])-1] += 1		

	numrides = opt(seats_load,customers_load)
	promotions = 0
	#print numrides
	#print seats_load
	for i in range(1,seats):
		promotions += max(seats_load[i]-numrides,0)
	#print promotions
		
	fo.write("Case #"+str(k+1)+": "+str(numrides)+' '+str(promotions)+"\n")
	print k
fo.close()
fi.close()