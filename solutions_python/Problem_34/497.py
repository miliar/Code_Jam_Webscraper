def main():

    l, d, n = raw_input().split()
    l = int(l)
    n = int(n)
    d = int(d)
    
    #d words follow
    dic = []
    for i in range(d):
        dic.append(raw_input())
    
    dic.sort()
    #print dic
    
    #n test cases follow
    for i in range(1,n+1):
        word = raw_input()
        count = 0
        #creates list of possible words
        list = [""]
        set = range(len(word))
        for ind in set:
            #print ind
            #sure letter
            if word[ind] != '(':
                list_aux = []
                for j in list:
                    list_aux.append(j + word[ind])
                list = list_aux
                
            #if ( is found, several possible letters follow
            else:
                list_aux = []
                set.remove(ind) #removes ( 
                ind += 1
                while word[ind] != ')':
                    #print "debug", word[ind], ind
                    #compute new possible words
                    for j in list:
                        for k in dic:
                            if k[:len(j)+1] == j + word[ind]:
                                list_aux.append(j + word[ind])
                                break
                            elif k[:len(j)+1] > j + word[ind]:
                                break
                        
                    #removes possible char from word
                    set.remove(ind) #removes (
                    ind += 1
                
                #no char from () matches word, exit
                if list_aux == []: break
                
                #recompute list with new possible words
                list = []
                for j in list_aux:
                    list.append(j)
        
        #searches for possible words in dictionary
        for j in list:
            if j in dic: count += 1
        
        #print "debug: ", list
        print "Case #" + str(i) + ": " + str(count)
                    
if __name__ == "__main__":
    main()
