'''
Created on 2009/9/3

@author: Cody
'''

filename = ['test','A-small-attempt0','A-small-attempt1','A-small-attempt2','A-small-attempt3']
filename = "A-large"
fin = open(filename+".in","r")
fout = open(filename+".out","w")
dictionary = {}
global match
def query(start,word,subpatterns,query_dictionary,length):
    try:
        global match
        query_dictionary[start]['exist']
        if length == L:
            match = match +1
            #print word
        else:
            for letter in subpatterns[0]:
                query(letter,word+letter,subpatterns[1:],query_dictionary[start],length+1)
    except KeyError:
        pass
if __name__ == '__main__':
    arg = fin.readline().split(" ")
    
    L = int(arg[0])
    D = int(arg[1])
    N = int(arg[2][:-1])
    temp = fin.readlines()
    words = map(lambda x:x[:-1],temp[0:D])
    patterns = map(lambda x:x[:-1],temp[D:])
    
    
    for word in words:
        now_dict = dictionary 
        parent = word[0:1]
        try:
            now_dict[parent]['exist'] = 1 
        except:
            now_dict[parent] = {'exist':1}
        for letter in word[1:]:
            child = letter
            child_dict = now_dict[parent]
            try:
                child_dict[child]['exist'] = 1 
            except:
                child_dict[child]={'exist':1}
            parent = child
            now_dict = child_dict
    #print dictionary
    
    #print dictionary['d']
    count = 0
    for pattern in patterns:
        print pattern
        count +=1
        match = 0
        index = 0 
        subpatterns = []
        while True:
            try:
                if(pattern[index]=='('):
                    right = pattern.find(')',index)
                    subpatterns.append(pattern[index+1:right])
                    index = right +1
                else:
                    subpatterns.append(pattern[index:index+1])
                    index = index+1
            except:
                break
        for letter in subpatterns[0]:
            query(letter,letter,subpatterns[1:],dictionary,1)
        #print "Case #"+str(count)+": "+str(match)
        fout.write("Case #"+str(count)+": "+str(match)+"\n")
    #print L,D,N
    #print words
    #print patterns
   
    pass
