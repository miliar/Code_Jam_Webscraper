def solve(N, M):
  # Method 1
  ans_1 = 0
  for i in range(1,N):
    ans_1 += max(0, M[i-1] - M[i])

  # Method 2
  ans_2 = 0
  max_gap = 0
  for i in range(1, N):
    max_gap = max(max_gap, M[i-1] - M[i])

  for i in range(N-1):
    ans_2 += min(max_gap, M[i])
  return str(ans_1) + " " + str(ans_2)

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")
    
if __name__ == '__main__':
  f = open('a.in')
  T = int(f.readline())
  answers = [0]*T
  for i in range(T):
    N = int(f.readline())
    line = f.readline()
    M = map(int, line.split(" "))
    answers[i] = solve(N, M)
  print_solution(answers)
  print answers
  print_solution(answers)

