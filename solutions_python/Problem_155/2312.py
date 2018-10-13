
def cal_status (max_level, status):
    stands = int(status[0]);
    require = 0;
    for i in range(1, max_level+1):
        if (stands >= i) :
            stands = stands + int(status[i]);
        else:
            diff = i - stands;
            stands = stands + int(status[i]) + diff;
            require = require + diff;

    return require;

results = [];
fp = open('A-large.in')
cases = int(fp.readline())
for i in range(0, cases):
  max_level, status = fp.readline().split();
  max_level = int(max_level);
  status = str(status);
  results.append(cal_status(max_level, status));

for i in range(1, cases+1):
    print ("Case #%d: %d" %(i, int(results[i-1])))
