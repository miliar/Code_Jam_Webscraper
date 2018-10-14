#!/usr/bin/env python

def is_palyndrome(number):
   list_ = [int(i) for i in list(str(number))]
   len_ = len(list_)
   is_ = True
   for e in range(len_/2 + 1):
      d = len_ -e -1
      if e > d:
         break
      if list_[e] != list_[d]:
         is_ = False
         break

   #print '%s %s' %(str(number), str(is_))
   return is_

def generate_palyndrome_list(start, end):
   return [x for x in range(start, end) if is_palyndrome(x)]

def only_fair_and_square(squared):
   return [x for x in squared if is_palyndrome(x)]

def how_many_in_the_range(numbers, start, end):
   total = 0
   for x in numbers:
      if x >= start and x <= end:
         #print 'X: %s' % str(x)
         total += 1
   return total

def analyse(range_):
   start = 1
   end = range_[1] + 1
   list_of_palyndromes = generate_palyndrome_list(start, end)
   #print list_of_palyndromes
   squared_palyndromes = [x**2 for x in list_of_palyndromes]
   fair_and_square = only_fair_and_square(squared_palyndromes)
   #print fair_and_square
   return how_many_in_the_range(fair_and_square, range_[0], range_[1])

def main():
   cases = int(raw_input())
   for case in range(cases):
      range_ = [int(i) for i in raw_input().split()]
      print 'Case #%s: %s' %(case+1, analyse(range_))
   pass

if __name__ == '__main__':
   main()
