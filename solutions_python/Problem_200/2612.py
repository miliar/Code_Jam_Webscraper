def check_tidy(l):
	n=len(l)-1
	pending = False
	for i in range(n):
		while l[i]>l[i+1] and not pending:
			l[i] = l[i] - 1
			pending = True
		if pending:
			l[i+1] = 9
	if pending:
		check_tidy(l)
def rlead_0(l):
	if l[0] == 0:
		return l[1:]
	else:
		return l
t=int(input())
case = 1
while case<=t:
	n=input()
	digit=[int(i) for i in n]
	check_tidy(digit)
	digit=rlead_0(digit)
	print("case #",case,":",sep="",end=" ")
	for i in digit:
		print(i,end='')
	print()
	case=case+1


