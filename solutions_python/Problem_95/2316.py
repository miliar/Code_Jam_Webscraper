from os import sys
mapping = {}
def train(output,input):
    for i in range(len(input)):
        if(not input[i] == ' '):
             mapping.update({output[i]: input[i]})

def translate(source):
    ret = ''
    for i in source:
        if(not str.isspace(i)):
            ret += mapping[i]
        else: ret+=i
            
    return ret

if __name__=="__main__":
   train("a zoo", "y qee")
   train("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")
   train("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
   train("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
   alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
   #look for missing letter
   missing = ''
   for i in alpha:
       if(not i in mapping.keys()):
          missing = i
          break
   for i in alpha:
        if(not i in mapping.values()):
           mapping.update({missing: i})
           break
   #print mapping
   #print translate("y qee")
   #open file
   source = file(sys.argv[1])
   sink = file(sys.argv[1].replace(".in","")+".out",'w')
   for c,i in enumerate(source):
          if(c>0):
              sink.write("Case #"+str(c)+": "+ translate(i))
   sink.close()
   source.close()
