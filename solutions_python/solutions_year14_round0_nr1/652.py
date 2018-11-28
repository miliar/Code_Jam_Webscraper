import sys
sys.stdin  = open("A-small-attempt0.in")
sys.stdout = open("A-small-attempt0.out", "w")
t = int(raw_input())
for case_no in range(1, t+1):
  guess = set(range(1, 17))
  for _ in range(2):
    ans = int(raw_input())
    for r in range(1, 5):
      nums = map(int, raw_input().split())
      if r == ans:
        guess = guess.intersection(nums)
  print "Case #%d: " % (case_no),
  if len(guess) == 0:
    print "Volunteer cheated!"
  elif len(guess) > 1:
    print "Bad magician!"
  else:
    print guess.pop()