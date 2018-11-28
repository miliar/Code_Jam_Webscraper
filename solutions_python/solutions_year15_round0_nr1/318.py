def convertToArray(s):
  S = []
  for i in range(len(s)):
    S.append(int(s[i]))
  return S

def solve(S, S_max):
  current_people_standing =0 
  people_to_add = 0
  for i in range(len(S)):
    print "iteration " + str(i)
    print "current_people_standing " + str(current_people_standing)
    if current_people_standing < i and S[i] > 0:

      print "added " + str(people_to_add)
      people_to_add += i - current_people_standing
      current_people_standing += i - current_people_standing
    current_people_standing += S[i]
    
  return people_to_add

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")
    

if __name__ == "__main__":
  f = open("A-large.in")
  T = int(f.readline());
  answers = [0]*T
  for i in range(T):
    line = f.readline()
    l = line.split(" ")
    S_max = l[0]
    S = l[1].strip()
    S = convertToArray(S)
    answers[i] = solve(S, S_max)
  print_solution(answers)
  print answers

