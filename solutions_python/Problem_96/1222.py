'''
Created on Apr 14, 2012

@author: kevin
'''

'''
N, number of googler
S number of suprising triples
p, value of at least of

N s P
'''

#f = open('testb.in', 'r')
#f = open('B-small-attempt0.in','r')
f = open('B-large.in','r')

num_entry = int(f.readline())

for i in range(num_entry):
    text = f.readline()
    values = map(int, text.split())
    num_g = values[0]
    num_suprise = values[1]
    min_value = values[2]
    
    no_suprise_min_total_score = min_value * 3 - 2
    suprise_min_total_score =  min_value * 3 - 3
    
    # sort score by highest
    scores = values[3:]
    scores.sort()
    scores.reverse()
    
    min_value_count = 0
    for score in scores:        
        avg = score / 3
        if (score >= no_suprise_min_total_score ):                    
            min_value_count += 1            
        else:            
            if (num_suprise > 0):
                if (score ==  0):
                    break           
                reminder = score % 3                
                if (reminder): # we can only shift if average is greater than 0
                    if (reminder == 1 and avg+ reminder >= min_value):
                        min_value_count += 1
                        num_suprise-=1
                    if (reminder == 2 and avg+ reminder >= min_value):
                        min_value_count += 1
                        num_suprise-=1
                elif (score >= suprise_min_total_score ): # if reminder is 0 we can still to x, x+1, x+2
                    min_value_count += 1
                    num_suprise-=1
                    
                    
    print "Case #%i: %i" %(i + 1,min_value_count )
            
    
        
        