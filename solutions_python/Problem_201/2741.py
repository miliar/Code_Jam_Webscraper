import sys
import math
f = open('out17c.out','w')
T = int( sys.stdin.readline().strip())
case=0
G ={}
G[1]=[0,0]
G[2]=[1,0]
G[3]=[1,1]

def GetSubCouple( _c):
	if _c in G:
		# print(_c, G[_c])
		return G[_c]
	else:
		D =math.floor(_c/2)
		G[_c] =[D,D-1] if _c %2 ==0 else [ D,D]
		# print( _c, G[_c])
		return G[_c] 


while( T>0 ):
	T-=1
	case+=1
	N , K= map(str,sys.stdin.readline().strip().split() )
	Nint= calc= int (N)
	Kint= int (K)
	NintTEST= int (N)
	resp= [0,Nint]
	lastR= [0,Nint]
	# print(Nint)
	count = 0
	# if Kint >1:
	deep = deepI =math.ceil( math.log(Kint+(1 if Nint%2 ==0 else 0 ),2))
	# print( GetSubCouple(calc,deep) )
	# print(deep)
	if deep ==0:
		resp= GetSubCouple( Nint)
	stack = [Nint]

	# print("es: ",deep)
	while Kint >0:
		# print(stack)
		# consult = max(max(resp) , min(lastR))
		# consult = max(lastR)

		consult =max(stack)
		stack.remove(consult)
		# lastR = resp
		resp = GetSubCouple(consult) 
		# print("evaluo ",consult," resp: ",resp)
		# stack.append(min(resp))
		stack.append(resp[0])
		stack.append(resp[1])
		# couple = G[1]
		# G[calc] = GetCouple(G,)
		# test= str(Nint)
		# deep-=1
		Kint-=1

	# print(deep)
	# print(deepI)
	# if resp != respTEST:
	# 	print("WARNIGN entrada", N, " obtuve ", resp, " esperaba ", respTEST)
	# print(resp)
	print    ("Case #"+str(case)+": "+str(resp[0])+" "+str(resp[1])          )
	f.write ("Case #"+str(case)+": "+str(resp[0])+" "+str(resp[1])+"\n")
	# break
f.close();
