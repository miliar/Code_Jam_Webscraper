#!/usr/bin/python

import re
import sys
import argparse
import csv
import urllib2


def readArgs():
  getOpt = argparse.ArgumentParser()
  
  getOpt.add_argument('-i', '--inFile',
      help='Read from file specified',
      action="store", nargs=1, required=True )

#  group = getOpt.add_mutually_exclusive_group()
#  group.add_argument('-m', '--male',
#      help='Write output to file: [inputfile].summary w/ male names',
#      action="store_true")
#  group.add_argument('-f', '--female',
#      help='Write output to file: [inputfile].summary w/ female names',
#      action="store_true")

  getOpt.add_argument('-o', '--outFile',
      help='File where you want to output the results',
      action="store", nargs=1, required=True )

  return getOpt.parse_args()


def getCallNum(bibnum, pattern):
 
  url="http://www.aadl.org/catalog/record/{bib}".format(bib=bibnum)
  response = urllib2.urlopen(url)
  the_page = response.read()
  
  match = pattern.findall(the_page) 

  if(not match):
    return ''
  else:
   
    if(len(match) > 1):
      print 'More than 1 match found!!'
  
    return match[0]
      

def main():

  args = readArgs()
  
  count = 0
  
  pattern = re.compile('Call number:\s*<strong>\s*<a.*>\s*(.*)</a>')
  
  with open(args.inFile[0], 'rb') as f_in, open(args.outFile[0], 'wb') as f_out:
    
    numTests = f_in.readline().strip('\n')

    for test in xrange( int(numTests) ):
      
      user1 = int( f_in.readline().strip('\n') )

      #READ CARDS
      cards1 = []

      for rownum in xrange(4):        
        cards1.append( f_in.readline().strip('\n').split() )
      
      user2 = int( f_in.readline().strip('\n') )
      
      cards2 = []

      for rownum in xrange(4):        
        cards2.append( f_in.readline().strip('\n').split() )

      intersect = set(cards1[user1 - 1]).intersection( cards2[user2 - 1] ) 
      
      ans = 'Case #' + str( test + 1 ) + ': '
      if( len(intersect) > 1 ):
        ans = ans + 'Bad magician!'
      elif( len(intersect) == 1 ):
        ans = ans + str( list(intersect)[0] )
      else:
        ans = ans + 'Volunteer cheated!'
      
      print ans
      f_out.write(ans + '\n')




if __name__ == '__main__':
  main()
