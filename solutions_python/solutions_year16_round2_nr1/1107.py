def get_uniqoue():
    words=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    words=["ONE", "THREE", "FIVE", "SEVEN", "NINE"]
    all_characters=''.join(words)
    all_characters=set(all_characters)
    
    for i in range(len(words)):
        word_characters=words[:i]+words[i+1:]
        word_characters=''.join(word_characters)
        word_characters=set(word_characters)
        print words[i],all_characters-word_characters
        
def create_character_dict(word):
    character_dict={'Z':0,'O':0,'W':0,'T':0,'U':0,'F':0,'X':0,'S':0,'G':0,'N':0}
    for character in word:
        try:
            character_dict[character]+=1
        except KeyError:
            character_dict[character]=1
    return character_dict
    
def get_number(character_dict):
    phone_number=[]
    good=True
    while good:
        good=False
        if character_dict['Z']>0:
            for temp in 'ZERO':
                character_dict[temp]-=1
            phone_number.append(0)
            good=True
        if character_dict['W']>0:
            for temp in 'TWO':
                character_dict[temp]-=1
            phone_number.append(2)
            good=True
        if character_dict['U']>0:
            for temp in 'FOUR':
                character_dict[temp]-=1
            phone_number.append(4)
            good=True
        if character_dict['X']>0:
            for temp in 'SIX':
                character_dict[temp]-=1
            phone_number.append(6)
            good=True
        if character_dict['G']>0:
            for temp in 'EIGHT':
                character_dict[temp]-=1
            phone_number.append(8)
            good=True
    good=True
    while good:
        good=False
        if character_dict['O']>0:
            for temp in 'ONE':
                character_dict[temp]-=1
            phone_number.append(1)
            good=True
        if character_dict['T']>0:
            for temp in 'THREE':
                character_dict[temp]-=1
            phone_number.append(3)
            good=True
        if character_dict['F']>0:
            for temp in 'FIVE':
                character_dict[temp]-=1
            phone_number.append(5)
            good=True
        if character_dict['S']>0:
            for temp in 'SEVEN':
                character_dict[temp]-=1
            phone_number.append(7)
            good=True
    good=True
    while good:
        good=False
        if character_dict['N']>0:
            for temp in 'NINE':
                character_dict[temp]-=1
            phone_number.append(9)
            good=True
    if sum(character_dict.values())!=0:
        print 'Problem!!!'
    phone_number.sort()
    return phone_number
    
def solve_problemA(fname):
    fin=open(fname)
    flines=fin.readlines()
    fin.close()
    fout=open(fname[:-3]+'.out','w')
    for i in range(1,len(flines)):
        print i
        word=flines[i].split()[0]
        number=get_number(create_character_dict(word))
        fout.write('Case #'+str(i)+': ')
        for n in number:
            fout.write(str(n))
        fout.write('\n')
    fout.close()

    
    
    

    
       
        
        
        
            
            
            
            
    
        
    
