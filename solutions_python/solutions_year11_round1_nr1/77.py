from fractions import Fraction
for c in range(1,input()+1):
    N,D,G = map(int, raw_input().split())
    if G==100:
        res="Broken" if D!= 100 else "Possible"
    elif G==0:
        res="Broken" if D!= 0 else "Possible"
    else:
        res="Possible" if  Fraction(D,100).denominator <= N else "Broken"
        
    
    
    print "Case #%s:"%c, res #,N,D,G, Fraction(D,100).denominator 
