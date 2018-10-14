import math

def range(start,stop):
   i = start
   while i < stop:
       yield i
       i += 1

f = open('A-large.in', 'r')
o = open('A-large.out', 'w')

T = int(f.readline().strip())



for t in xrange(T):
    (A0,A1,A2,A3) = map(str, f.readline().strip())
    (B0,B1,B2,B3) = map(str, f.readline().strip())
    (C0,C1,C2,C3) = map(str, f.readline().strip())
    (D0,D1,D2,D3) = map(str, f.readline().strip())
   
    #print A0+A1+A2+A3
    #print B0+B1+B2+B3
    #print C0+C1+C2+C3
    #print D0+D1+D2+D3
	
    result = "Game has not completed"	
    
    winA = A0+A1+A2+A3
    winB = B0+B1+B2+B3
    winC = C0+C1+C2+C3
    winD = D0+D1+D2+D3
    win0 = A0+B0+C0+D0
    win1 = A1+B1+C1+D1
    win2 = A2+B2+C2+D2
    win3 = A3+B3+C3+D3
    wind1 = A0+B1+C2+D3
    wind2 = A3+B2+C1+D0

    if all(x != "." for x in (A0, B0, C0, D0, A1, B1, C1, D1, A2, B2, C2, D2, A3, B3, C3, D3)):
		result = "Draw"

    if any(x == "XXXX" or x == "TXXX" or x == "XTXX" or x == "XXTX" or x == "XXXT" for x in (winA, winB, winC, winD, win0, win1, win2, win3, wind1, wind2)):
		result = "X won"

    if any(x == "OOOO" or x == "TOOO" or x == "OTOO" or x == "OOTO" or x == "OOOT" for x in (winA, winB, winC, winD, win0, win1, win2, win3, wind1, wind2)):
		result = "O won"
	

	
    s = "Case #%d: %s\n" % (t+1, result)
    print s
    o.write(s)
    f.readline()	


