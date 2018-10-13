# Google Code Jam 2017 Qualifying C
'''
Each user divides largest space in half.  Placing 10^18 (a quintillion)
users one at a time seems like it could be slow.  We don't need to use
the algorithm given in the problem, just determine numerically how
crowded it'll be.
N  K
10 1 => 5 4
10 2 => 2 2
10 3 => 1 0
Each time I place somebody I cut the search space in half.  So I can
do lg(K) operations rather than K.
At step s we place 2^s more users and divide each space in half.
60 steps will do 10^18 users.  I've got this.  But each step there are
some holes h wide, and some h+1.  I need to know after the last step
how many of each.
Step Placed Holes
0    0      10
1    1      5,4
2    3      2,1
3    7      1,0

N K              hole size (before)
1:1 0,0             1
2:1 1,0             2
  2 0,0             1
3:1 1,1  .x.        3
  2 0,0  xx.        1
  3 0,0             1        
4:1 2,1  .x..       4
  2 1,0  .xx.       2
  3 0,0  xxx.       1
  4 0,0  xxxx       1
5:1 2,2  ..x..      5
  2 1,0  x.x..      2
  3 1,0  x.xx.      2
  4 0,0  xxxx.      1
  5 0,0  xxxxx      1
6:1 3,2  ..x...     6
  2 1,1  ..x.x.     3
  3 1,0  x.x.x.     1
  4 0,0  xxx.x.     1
  5 0,0  xxxxx.     1
  6 0,0  xxxxxx     1
7:1 3,3  ...x...    7
  2 1,1  .x.x...    3
  3 1,1  .x.x.x.    3
  4 0,0  xx.x.x.    1
  5 0,0  xxxx.x.    1
  6 0,0  xxxxxx.    1
  7 0,0  xxxxxxx    1
answer = (hole/2, (hole-1)/2)
hole = hole/2 usually
12:1 6,5 .....x...... 12 1
   2 3,2 .....x..x... 6
   3 2,2 ..x..x..x... 3  1+2
   4 1,1 ..x..x..x.x. 2
   5 1,0 x.x..x..x.x. 2
   6 1,0 x.xx.x..x.x. 2
   7 1,0 x.xx.xx.x.x. 2  1+2+4
   8 0,0 xxxx.xx.x.x. 1
   9 0,0 xxxxxxx.x.x. 1
  10 0,0 xxxxxxxxx.x. 1
  11 0,0 xxxxxxxxxxx. 1
  12 0,0 xxxxxxxxxxxx 1
For N:12 K:8
Start at 7.  Find hole for 7.
1 6
2 3
3 1 hole:1 answer:(0,0)
Wait, if we go to K/2 quickly then add one user at a time, when K ==
10**18 we have 10**17 steps to do manually.  Actually in that case
hole would probably be 1 so we'd already have the answer.  But the
edge of (2,1) vs. (1,1) could be hard.  But I could do the two small
datasets.
Can we do this backwards?  Last N/2 are all (0,0).  Next N/4 are (1,0)?
I could go naive and store map of hole size to count.  OK, I'm giving
up on being efficient and doing that.
12:1
6:1 5:1
5:1 3:1 2:1
3:1 2:3
2:3 1:2
2:2 1:3
2:1 1:4
1:5
'''
class Holes(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 0
    def increment(self, key):
        if key in self:
            self[key] += 1
        else:
            self[key] = 1
    def decrement(self, key):
        self[key] -= 1
        if self[key] == 0:
            del self[key]
    def largest(self):
        return max(k for k, v in self.iteritems() if v)
def do(N, K):
    holes = Holes()
    holes[N] = 1
    users = 1                   # hack
    while users < K:
        if holes.largest() <= 1:
            return (0,0)
        users += 1
        largest = holes.largest()
        holes.decrement(largest)
        holes.increment(largest/2)
        holes.increment((largest-1)/2)
    largest = holes.largest()
    return (largest/2, (largest-1)/2)

def doCase(s):
    return do(int(s[0]), int(s[1]))

cases = int(raw_input())
for i in range(cases):
    pair = doCase(raw_input().strip().split())
    print 'Case #{}: {} {}'.format(i+1, pair[0], pair[1])
