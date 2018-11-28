#!/usr/bin/env python

f=open('input.txt','r')

lang=[]

firstline = f.readline()

wordSize=firstline.strip().split(' ')[0]
wordCase=firstline.strip().split(' ')[1]
lineToRead=firstline.strip().split(' ')[2]

def check(langItem,toCheck):
 rc=True 
 wordArray=splitItem(toCheck) 
 for i in range(0, len(langItem)):
  if wordArray[i].lower().count(langItem[i])==0:
   rc=False
 return rc

def splitItem(input):
 toReturn=[]
 tempWord=''
 record=False
 for i in range(0, len(input)):
  if input[i]=='(':
   record=True 
  elif record==True and input[i]!='(' and input[i]!=')':
   tempWord=tempWord + input[i]
  elif input[i]==')':
   toReturn.append(tempWord)
   record=False
   tempWord=''
  elif record==False and input[i]!='(' and input[i]!=')':
   toReturn.append(input[i])
 return toReturn 


def insertLang():
 #getting lang into lang array
 for count in range(0, int(wordCase)):
  lang.append(f.readline().strip())
  #print lang

def startProc():
 #Starting processing from test case line
 for count in range(0, int(lineToRead)):
  tally=0
  tempLine=f.readline()
  for num in range(0, len(lang)):
   #print check(lang[num],tempLine)
   if check(lang[num],tempLine)==True:
    tally=tally+1
  print "Case #" + str(count+1) + ": " + str(tally)

"""
splitItem('(ab)(bc)(ca)')
splitItem('(zyx)bc')
splitItem('abc')
splitItem('(abc)(abc)(abc)')
check('cba','(ab)(bc)(ca)')
"""
insertLang()
startProc()
