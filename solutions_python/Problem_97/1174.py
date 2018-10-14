#Recylced.py
#Justin Roberts (tangofox10@gmail.com)
#Google Code Jam Qualification Round
#Problem: Recycled Numbers
#Written in Python

#Ah. I slept about 9 hours there.
#Just what I needed.
#I'm getting over a case of bronchitis so rest is good.

#Alright. This looks like it should be a double-digit Project Euler problem.
#Cool, I'm going to brute force this guy.

fin = open('C-small-attempt0.in', 'r')
fout = open('RecycledOut.txt', 'w')

T = int(fin.readline())

#Wait, on the large data set 1 ≤ A ≤ B ≤ 2000000... so B-A could be up to 1M.
#Brute forcing seems to be O((B-A)^2) time so... eh... I might have to
#make this thing a little bit smarter to do that one right.
#Not sure though... I mean, the 8 minute time limit is kind of long.

#ok, checking if two numbers are recycled are easy. The key word root is
#"cycle." The two numbers must be the same length and one must be a cyclic
#transposition of the other.
def are_recycled(x,y):
    if x < 10:
        return 0
    a = []
    while x > 0:
        a.append(x%10)
        x //= 10
    b = []
    while y > 0:
        b.append(y%10)
        y //= 10
    for i in range(len(b)):
        if b[i] == a[0]:
            j = 1
            if j + i == len(b):
                j = -i
            while j != 0:
                if b[i+j] != a[j]:
                    break
                j += 1
                if j + i == len(b):
                    j = -i
            else:
                return 1
    return 0

for case in range(1,T+1):
    result = 0
    (A,B) = map(int,fin.readline().split())
    for x in range(A,B+1):
        for y in range(x+1,B+1):
            if are_recycled(x,y):
                result += 1
    fout.write('Case #%d: %d\n'%(case,result))
    print('Case #%d: %d'%(case,result))

#Oh goody! I wrote something wrong. Time to put on my debugger hat!

#Oh gosh. I put result outside my case loop! It wasn't zeroing out.
#I'm such an idiot.

#Hmm... this thing is certainly moving fast enough for the small data set.
#However, it'll probably be crushed by the large. T_T
#Yeah, right about 9 seconds for case 4 of the sample. That's way too slow.

#Oh, and the output from problem B was much less entertaining than the one
#from problem A. I am disappointed.

