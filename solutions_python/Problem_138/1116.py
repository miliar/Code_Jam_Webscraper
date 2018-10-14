def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    n = int(input())
    naomi = list(map(float, input().split()))
    ken = list(map(float, input().split()))
    naomi.sort()
    ken.sort()
    print("Case #%i: %d %d" % (caseNr, deceitfulWar(naomi,ken), war(naomi,ken)))

def deceitfulWar(naomi,ken):
  j = 0
  c = 0
  for i in range(len(naomi)):
    if naomi[i] < ken[j]:
      c += 1
    else:
      j += 1
  return len(naomi)-c

def war(naomi,ken):
  c = 0
  for i in range(len(naomi)):
    for j in range(len(ken)):
      if naomi[i] < ken[j]:
        break
      else:
        c += 1
    ken = ken[j+1:]
    if len(ken) == 0:
      break
  return c

if __name__ == "__main__":
  main()
