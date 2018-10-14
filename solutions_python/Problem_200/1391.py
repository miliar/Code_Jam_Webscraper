def printList(l):
  for e in l:
    print(e, end = "")
  print()

def removeZeros(l):
  while l[0] == 0:
    del l[0]

T = int(input())
for i in range(T):
  N = list(input())
  N = [int(j) for j in N]
  j = len(N) - 2
  end = len(N)
  while j >= 0:
    if N[j] > N[j + 1]:
      N[j] -= 1
      k = j + 1
      while k < end:
        N[k] = 9
        k += 1
      end = j + 1
    j -= 1
  print("Case #" + str(i + 1) + ": ", end = "")
  removeZeros(N)
  printList(N)