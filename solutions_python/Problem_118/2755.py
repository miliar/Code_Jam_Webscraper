def main():
  numCases = int(input())
  for case in range(numCases):
    count = 0
    Min, Max = input().split()
    Min = int(Min)
    Max = int(Max)
    for i in range(Min, Max+1):
      test = i**0.5
      if int(test) == test:
        if str(i) == str(i)[::-1]:
          if str(int(test)) == str(int(test))[::-1]:
            count += 1
    print("Case #"+str(case+1)+": "+str(count))

if __name__ == "__main__": main()
