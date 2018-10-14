# Carly Smith
# Google Code Jam 2017
def pancake_flips():
  with open('A-large.in') as f:
    content = f.readlines()

  content = [x.strip("\n") for x in content]

  T = int(content[0])

  for i in range(1,T+1):
    S, K = content[i].split()
    K = int(K)

    num_flips = traverse_pancakes(S, K)

    print 'Case #{0}: {1}'.format(i, num_flips)

def traverse_pancakes(S, K):
  count_flips = 0
  for i in range(0, len(S)):
    if S[i] == '-':
      if i + K <= len(S):
        S = flip(S, K, i)
        count_flips += 1
      else:
        return 'IMPOSSIBLE'

  for i in S:
    if i == '-':
      return 'IMPOSSIBLE'

  return count_flips

def flip(S, K, i):
  for i in range(i, i+K):
    if S[i] == '+':
      S = S[0:i] + '-' + S[i+1: len(S)]
    else:
      S = S[0:i] + '+' + S[i+1: len(S)]

  return S

if __name__ == "__main__":
  pancake_flips()
