

def ch(al):
    l =[]
    while "Z" in al:
        l.append('0')
        for s in 'ZERO':
            ind = al.index(s)
            al.pop(ind)
    while "X" in al:
        l.append('6')
        for s in 'SIX':
            ind = al.index(s)
            al.pop(ind)
def ch(al):
    l =[]
    while "Z" in al:
        l.append('0')
        for s in 'ZERO':
            ind = al.index(s)
            al.pop(ind)
    while "X" in al:
        l.append('6')
        for s in 'SIX':
            ind = al.index(s)
            al.pop(ind)
    while "W" in al:
        l.append('2')
        for s in 'TWO':
            ind = al.index(s)
            al.pop(ind)
    
    while "G" in al:
        l.append('8')
        for s in 'EIGHT':
            ind = al.index(s)
            al.pop(ind)
    while "U" in al:
        l.append('4')
        for s in 'FOUR':
            ind = al.index(s)
            al.pop(ind)
    while "O" in al:
        l.append('1')
        for s in 'ONE':
            ind = al.index(s)
            al.pop(ind)
    while "S" in al:
        l.append('7')
        for s in 'SEVEN':
            ind = al.index(s)
            al.pop(ind)
    while "V" in al:
        l.append('5')
        for s in 'FIVE':
            ind = al.index(s)
            al.pop(ind) 
    while "N" in al:
        l.append('9')
        for s in 'NINE':
            ind = al.index(s)
            al.pop(ind)  
    while "T" in al:
        l.append('3')
        for s in 'THREE':
            ind = al.index(s)
            al.pop(ind)  
            
    l.sort()
    return l  
            
            
            
            
            
            
            
   

            
   

            
            
            
t= int(raw_input())
for i in range(t):
     
   print "Case #"+str(i+1)+": "+''.join((ch(list(raw_input()))))
              
            
            
            
   

