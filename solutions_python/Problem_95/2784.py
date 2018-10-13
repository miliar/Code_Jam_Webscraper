'''
Created on 14.04.2012

@author: admin
'''


dic = {'a': 'y', 'o': 'e', 'z': 'q'}

new_dict = dict([(dic[k], k) for k in dic.keys()])

def get_dict():
   str_in = ['ejp mysljylc kd kxveddknmc re jsicpdrysi'
   , 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
   , 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
   
   str_out = ['our language is impossible to understand'
   , 'there are twenty six factorial possibilities'
   , 'so it is okay if you want to just give up']
   
   dicct = {}
   for i in range(0, len(str_in)):
      #print str_in[i]
      string = str_in[i]
      for j in range(0, len(string)):
         dicct[str_in[i][j]] = str_out[i][j]
         
   return dicct


def translate(string, dic):
   out = ''
   for s in string:
      if s in dic:
         out = out + dic[s]
      else:
         out = out + s
   
   return out


f_in = open('A-small-attempt1.in', 'r')
f_out = open('A-small-attempt1.out', 'w')

count = -1
for line in f_in:
   count = count + 1

   if count == 0:
      continue
   
   #print line[:-1]
   
   dicc = get_dict()
   dicc['z'] = 'q'
   dicc['q'] = 'z'
   
   s = 'Case #' + str(count) + ': ' + translate(line[:-1], dicc)
   print s
   f_out.write(s + '\n')
   
f_in.close()
f_out.close()


#Input
#3
#ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv
#
#
#Output
#Case #1: our language is impossible to understand
#Case #2: there are twenty six factorial possibilities
#Case #3: so it is okay if you want to just give up






