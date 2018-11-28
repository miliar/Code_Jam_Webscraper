#include <iostream>
#include <map>

void print(int caseNum, long output1, long output2) {
  std::cout << "Case #" << caseNum << ": " << output1 << " " << output2 << std::endl;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    long N, K;
    scanf("%ld %ld", &N, &K);

    std::map<long, long> spaces;
    std::map<long, long>::reverse_iterator maxIt;
    spaces[N] = 1;

    while (K > 0) {
      maxIt = spaces.rbegin();
      long maxSpace = maxIt->first;
      long maxSpaceCount = maxIt->second;
      long ls = (maxSpace-1) / 2;
      long rs = maxSpace / 2;

      if (maxSpaceCount >= K) {
        print(t, rs, ls);
      } else {
        if (ls == rs) {
          spaces[ls] += 2*maxSpaceCount;
        } else {
          spaces[ls] += maxSpaceCount;
          spaces[rs] += maxSpaceCount;
        }
        spaces.erase(maxSpace);
      }
      K -= maxSpaceCount;
    }
  }

  return 0;
}
