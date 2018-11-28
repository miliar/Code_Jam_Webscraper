ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9

def findNum(S, numStr, count):
  for c in numStr:
    S = S.replace(c, "", count)
  return S

def main():
  T = int(raw_input())
  for t in xrange(T):
    S = raw_input()
    ans = ""
    one = three = 0
    count = S.count("Z")
    S = findNum(S, "ZERO", count)
    ans += "0"*count
    one = count

    count = S.count("W")
    S = findNum(S, "TWO", count)
    ans += "2"*count
    three = len(ans)

    count = S.count("U")
    S = findNum(S, "FOUR", count)
    ans += "4"*count
    count = S.count("F")
    S = findNum(S, "FIVE", count)
    ans += "5"*count
    count = S.count("X")
    S = findNum(S, "SIX", count)
    ans += "6"*count
    count = S.count("V")
    S = findNum(S, "SEVEN", count)
    ans += "7"*count
    count = S.count("G")
    S = findNum(S, "EIGHT", count)
    ans += "8"*count
    count = S.count("I")
    S = findNum(S, "NINE", count)
    ans += "9"*count
    count = S.count("T")
    S = findNum(S, "THREE", count)
    ans = ans[:three] + "3"*count + ans[three:]

    count = S.count("O")
    S = findNum(S, "ONE", count)
    ans = ans[:one] + "1"*count + ans[one:]

    print "Case #{}: {}".format(t+1, ans)

if __name__ == "__main__":
  main()
