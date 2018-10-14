def solve(X, R, C):
  if X >= 7:
    return "RICHARD"
  elif (R*C) % X != 0:
    return "RICHARD"
  elif X > R and X > C:
    return "RICHARD"
  elif (X + 1)// 2 > min(R, C):
    return "RICHARD"
  elif X == 4:
    return "GABRIEL" if min(R, C) > 2 else "RICHARD"
  elif X == 5:
    return "GABRIEL" if not(min(R,C) == 3 and max(R,C) == 5) else "RICHARD"
  elif X == 6:
    return "GABRIEL" if min(R, C) > 3 else "RICHARD"
  else:
    return "GABRIEL"

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")
    
if __name__ == '__main__':
  f = open('D-large.in')
  T = int(f.readline())
  answers = [0]*T
  for i in range(T):
    line = f.readline()
    P = map(int, line.split(" "))
    X = P[0]
    R = P[1]
    C = P[2]
    answers[i] = solve(X,R,C)
  print_solution(answers)
  print answers

