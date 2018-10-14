'''
Created on 12 mai 2013

@author: Regis
'''

VOYELS = set('aeiou')

def has_consecutive_consonants(word, n):
    count = 0
    for c in word:
        if c in VOYELS:
            count =0
        else:
            count +=1
            if count >=n:
                return True
    return False

    
def nlength(word, n):
    '''
    Returns the number of substring which have at least n consecutive consonants
    '''
    nb_consons = sum (((0 if c in VOYELS else 1) for c in word))
    
    count = 0
    
    stack = []
    stack.append((False, 0, len(word)-1))
    
    processed=set()
    
    while stack:
        (consec_consons, start, end) = stack.pop()
        if start > end:
            continue
        if (start,end) in processed:
            continue
        w=word[start:end+1]
        if not consec_consons and not has_consecutive_consonants(w, n):
            continue
        processed.add( (start,end) )
        #print(w)
        
        # nb_consons >=n
        count += 1
        # try substrings from this
        # I can't reduce the number of consonants
        stack.append((word[start] in VOYELS, start + 1, end))
        stack.append((word[end] in VOYELS, start, end - 1))
    return count

if __name__ == '__main__':
    with open('A-small-attempt1.in') as f:
        n = int (f.readline())
        for i in range(1, n + 1):
            line = f.readline().rstrip()
            line = line.split(' ')
            print("Case #{i}: {nb}".format(i=i, nb=nlength(line[0], int(line[1]))))
