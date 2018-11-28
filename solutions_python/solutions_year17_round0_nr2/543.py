import sys

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  for i in range(1, t+1):
    val = list(data[i].strip("\n"))
    val = map(lambda x: int(x), val)
    for k in range(1, len(val))[::-1]:
      if val[k] < val[k-1]:
        val[k] = 9
        val[k-1] -= 1
      	if k+1 < len(val) and val[k+1] < val[k]:
          for j in range(k+1, len(val)):
            val[j] = 9
    ret = map(lambda x: str(x), val)
    ret = "".join(ret).strip("0")
    print("Case #%d: %s" % (i, ret))
