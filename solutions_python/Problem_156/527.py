answer = float('inf')

def F(Pi, count, carry=[]):
	global answer

	if count < answer:
		item = max(Pi)
		if item == 0:
			answer = min(answer, count)

		elif item < 4:
			F([x-item for x in Pi], count+item, carry + [(-1, Pi)])	

		else:
			# normal day
			F([x-1 for x in Pi], count+1, carry + [(-1, Pi)])

			# special day
			Pi_2 = [x for x in Pi]
			index = Pi.index(item) 

			Pi_2[index] = item/2 + item%2
			Pi_2.append(item/2)

			F(Pi_2, count+1, carry + [(item, Pi)])

			#--
			Pi_2 = [x for x in Pi]
			index = Pi.index(item) 

			Pi_2[index] = 3
			Pi_2.append(item-3)

			F(Pi_2, count+1, carry + [(item, Pi)])

T = int(raw_input())

for test in range(1, T+1):

	D = int(raw_input())
	P = map(int, raw_input().split())
	answer = max(P)

	F(P, 0)

	print "Case #{}: {}".format(test, answer)

"""
5 4 5 4 5 4


... + 5

1
-
2
-
3
-
 4
2  2
-
5
3 2
-
6
3 3
- *
 7
 6
3  3 
-
  8
 4   4
2 2  2 2
-
    9
 5    4
3 2  2 2



6
3 3


              15

     7              8
  3      4        4      4
       2    2   2   2   2  2


                 22
         11
    5          6
  3   2     3     3


                26

       13
   6        7
 3    3   3    4
              2   2

       13
       12
   6        6
 3    3   3   3

"""