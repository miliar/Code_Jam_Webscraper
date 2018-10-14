import re

def process(dic,reg):
   pattern = reg.replace('(','[').replace(')',']')
   count = 0
   for i in range(0,len(dic)):
      if (re.search(pattern,dic[i])):
         count+=1
   return count

def main():
   dic = []
   numbers = raw_input().split(' ')
   for i in range(0,int(numbers[1])):
      dic.append(raw_input())
   
   for i in range(0,int(numbers[2])):
      word = raw_input()
      count = process(dic,word)
      print "Case #%d: %d" % (i+1,count)
   

if __name__ == "__main__":
   main()
