from bisect import *

def is_palyndrome(word):
    for i in range(len(word)/2):
        if word[i] != word[len(word)-i-1] :
            return False
    return True

"""
Generate all palyndromes < 8 characters
"""
def generate_all_palyndrome():
    l = []

    # length 1
    l.extend(xrange(1,10))
    
    # length 2
    for i in xrange(1,10):
        l.append(str(i)+str(i))
        
    # length 3
    for i in xrange(1,10):
        for j in xrange(0,10):
            l.append(str(i)+str(j)+str(i))
            
    # length 4
    for i in xrange(1,10):
        for j in xrange(0,10):
            l.append(str(i)+str(j)+str(j)+str(i))
            
    # length 5
    for i in xrange(1,10):
        for j in xrange(0,10):
            for k in xrange(0,10):
                l.append(str(i)+str(j)+str(k)+str(j)+str(i))
                
    # length 6
    for i in xrange(1,10):
        for j in xrange(0,10):
            for k in xrange(0,10):
                l.append(str(i)+str(j)+str(k)+str(k)+str(j)+str(i))
                
    # length 7
    for i in xrange(1,10):
        for j in xrange(0,10):
            for k in xrange(0,10):
                for m in xrange(0,10):
                    l.append(str(i)+str(j)+str(k)+str(m)+str(k)+str(j)+str(i))
                    
    # length 8
    for i in xrange(1,10):
        for j in xrange(0,10):
            for k in xrange(0,10):
                for m in xrange(0,10):
                    l.append(str(i)+str(j)+str(k)+str(m)+str(m)+str(k)+str(j)+str(i))
    
    return l
    
    
def generate_all_square_palyndromes():
    palyndromes = generate_all_palyndrome()
    square_palyndromes = []
    
    for p in palyndromes :
        word = str(int(p)*int(p))
        if is_palyndrome(word):
            square_palyndromes.append(int(word))
            
    return square_palyndromes

with open("C-small-attempt0.in") as f:
            
    sq_palyn = generate_all_square_palyndromes()
    
    for turn in range(1, int(f.readline())+1) :
        l = f.readline().split()
        x, y = int(l[0]), int(l[1])

        i = bisect_right(sq_palyn, x) - 1
        j = bisect_left(sq_palyn, y)
        
        nb_sq_palyn = (j-i-1) + (sq_palyn[i]==x) + (sq_palyn[j]==y)

                    
        print "Case #%d:" %turn, "%d" % nb_sq_palyn
