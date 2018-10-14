#main
#input section
T = input()
for i in xrange(0,T):
   O = []
   o_count = 0
   B = []
   b_count = 0
   goals = []
   s = []
   z = raw_input()
   s = z.split(' ')
   N = int(s[0])
   for j in xrange(0,N):
      if s[1+j*2]=='O':
         O.append(int(s[2+j*2]))
         o_count+=1
      else:
         B.append(int(s[2+j*2]))
         b_count+=1
      goals.append([s[1+j*2],int(s[2+j*2])])
   #print 'O : ',O
   #print 'B : ',B
   #print goals
#end input section
   o_place, b_place = 1, 1
   step = 0
   while N>0:
    done = 0
    if o_count>0:
      if o_place<O[0]:
         o_place+=1
      else:
         if o_place>O[0]:
            o_place-=1
         else:
            if goals[0][0]=='O':
               goals=goals[1:]
               O=O[1:]
               o_count-=1
               N-=1
               done = 1
    if b_count>0: 
      if b_place<B[0]:
         b_place+=1
      else:
         if b_place>B[0]:
            b_place-=1
         else:
           if (N>0):# and (done==0):
            if goals[0][0]=='B' and done==0:
               goals=goals[1:]
               B=B[1:]
               b_count-=1
               N-=1
               #if N>0:
               #  if goals[0][0]=='O':
               #    if goals[0][1]==o_place:
               #      O=O[1:]
               #      o_count-=1
               #      N-=1
               #else: break
    step+=1
    iii = i+1
   print 'Case #%i:'%iii, step

