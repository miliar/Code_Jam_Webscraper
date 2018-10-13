import sys, operator, string

def Nach (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] > Ele:
			return Vek[i]
	return -1

def S2L (Str):
	List = []
	for i in range (len (Str)):
		if Str[i] in '1234567890':
			List.append (int(Str[i]))
	return List

def L2S (List):
	Str = ''
	for i in range (len (List)):
		Str = Str + str(List[i])
	return Str

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	N = sys.stdin.readline()
	V = S2L (N)
	VL = len(V)

	i = VL-2
	while (i>=0) & (V[i]>=V[i+1]): i = i-1
	if i==-1:
		Vnew = V + [0]
		Vnew.sort()
		aNew = Nach (Vnew, 0)
		Vnew.remove (aNew)
		Y = [aNew] + Vnew
	else:
		a = V[i]
		First = V[:i]
		Reord = sorted (V[i:])
		aNew = Nach (Reord, a)
		Reord.remove (aNew)
		Y = First + [aNew] + Reord

	K = L2S (Y)
	Str = "Case #" + str(X) + ": " + K
	print Str
	sys.stdout.flush()
