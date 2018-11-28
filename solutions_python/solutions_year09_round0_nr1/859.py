file = open("small.in","r")
words = []
pattern = {0:'',1:'',2:'',3:'',4:'',5:''}
i = 1
#print pattern[i]
constant = {0:'',1:'',2:'',3:'',4:'',5:''} 
flag = 0
line = file.readline()
l = int(line.split()[0])
d = int(line.split()[1])
n = int(line.split()[2])
#print l,d,n

for i in range(d) :
    word = file.readline().strip('\n')
    words.append(word)
#print words


def func(pattern,constant) :
    pword = []
    for letter in pattern :
        pword.append( letter  + constant)
    return pword

for t in range(n) :
  test = file.readline().strip('\n')
  #print  test
  if (test.find('(')>=0) :
    if test.startswith('(') :
        start = ''
        pass
    else :
        start = test.split('(')[0]
        flag = 0
        for word in words :
            if word.startswith(start):
                flag = 1
                break
        if flag == 0 :
            print "no matches"
            continue
        test = test.split(start)[1]
    testcase =  []
    pattern = {}
    constant = {}
    possible = []
    pword = {}
    j = -1
    k = -1
    for letter in test :
        testcase.append(letter)
    for letter in testcase :
        if letter ==  '(' :
            flag = 1
            j = j + 1
            pattern[j]=''
        if letter == ')' :
            flag  = 0
            k= k + 1
            constant[k]=''
        else :
            if flag == 1 :  
                pattern[j] = pattern[j] + letter
            else :
                constant[k] = constant[k] + letter
    for z in range(k+1):
        pattern[z] = pattern[z].lstrip('(')
        #print  "pattern="  , pattern[z] , "constant=" , constant[z]
        pword[z] =  func(pattern[z],constant[z]) 
        #print pword[z],z    

    if j==9 : 
        count = 0
        for word in words :
            flag =  0 
            i = 0
            for letter in word :
            #print letter,pword[i]
                if letter in pword[i] :
                    pass
                else :
                    flag = 1
                    break
                i = i + 1 
            if flag  == 1 :
                pass
            else :
                count = count + 1



        print "Case #" ,  t + 1 , ": " ,  count
        continue





            
    else :
     if z > 0: 
      count = 1
      temp  = pword[0]
      while count <  (z+1) :
        possible = []
        #print "temp:",temp
        #print "pword:",pword[count]
        for domain in temp :
            #print domain
            for value in pword[count] :
                #print value
                possible.append(domain + value)
        count = count + 1
        temp = possible
    
     else :
        possible = pword[z]
        
  else :
      possible = []
      start = ''
      possible.append(test)
  #print possible
  number = 0
  for word in possible  :
      word = start + word
      if word in words :
            number = number + 1
            
    
  print "Case #",t + 1,": " ,  number
