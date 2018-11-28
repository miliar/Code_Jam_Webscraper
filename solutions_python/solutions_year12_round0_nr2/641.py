# Call a "good" triple one with max(t) >= p.
# Call a "surprising" triple one with max(t) - min(t) = 2.

# Rule 1: Any triple that can be unsurprisingly good can also be surprisingly good.
# Proof:
# Let a,b,c=ordered(t)
# if max(t)-min(t) = 1, then a=b or b=c (otherwise a<b<c in order implies c-a = 2).
# If a=b, then max(t)=c, and a--/b++ won't affect c, and results in surprise.
# If b=c, then b--/c++ will improve the best score and add surprise.

# Therefore, cost function: Determine triples that can be unsurprisingly good: A
# Determine triples that can only be surprisingly good: B
# A + min(surprising, B) = X.

# An unsurprising triple always has the form x,x,x or x,x,x+1 or x,x+1,x+1.
# SUM(t) = 3x, 3x+1, 3x+2
# Therefore each total score has EXACTLY ONE unsurprising triple:
# SUM/3, SUM/3 + (SUM%3)/2, SUM%3 + min(1, SUM%3)
# Or: A = SUM(x) / 3, B = (SUM(X)-A) / 2, C = SUM(X)-A-B

# A surprising triple always has the form x,x,x+2, x,x+1,x+2 or x,x+2,x+2.
# A surprising triple can be made unsurprising by equalizing the two outside scores.
# x+1,x,x+1  or x+1, x+1, x+1 or x+1, x+2, x+1
# Vice versa, an unsurprising triple can receive surprise (see above) by
# unbalancing two equal values (and only like that).

# Therefore, the maximum unsurprising value of a triple is x/3 + (x%3 > 0)
# The maximum surprise bonus of a triple is 1, IF x%3 != 1.

# Example: p=5
# 15: 5,5,5     (15+2)/3=5
# 14: 5,5,4     (14+2)/3=5
# 13: 5,4,4     (13+2)/3=5
# 12: 5,4,3(!)  (12+4)/3=5
# 11: 5,3,3(!)  (11+4)/3=5
# 10: ------

# Example: p=2
# 7: 2,2,3
# 6: 2,2,2
# 5: 2,2,1
# 4: 2,1,1
# 3: 2,1,0(!)
# 2: 2,0,0(!)
# 1: -----

# Example: p=1
# 4: 2,1,1
# 3: 2,1,0
# 2: 1,1,0
# 1: 1,0,0
# 0: 1,0,-1 BADBADBAD. Edgecase. Surprise cannot raise 0 to 1.

# And now, start.

def maxbest(totals, surprises, p):
  result = 0
  for t in totals:
    if t+2 >= 3*p:
      result += 1
    elif surprises > 0 and t+4 >= 3*p and t > 0:
      result += 1
      surprises -= 1
  return result


t = int(raw_input())

for i in range(t):
  line = map(int, raw_input().split())
  s,p,totals = line[1], line[2], line[3:]
  print "Case #%d: %s" % (i+1, maxbest(totals, s, p))


