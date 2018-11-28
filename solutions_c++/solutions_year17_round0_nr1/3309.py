#include <bitset>
#include <fstream>

int computeMinFlips(const std::string &S, const int&K) {
  // S is a string like ---+++--
  // K is size of pancake flipper
  // return min number of flips to get to all +'s
  std::bitset<1000> bs {};
  int L = S.length();
  for (int i=0;i<L;++i) {
    if (S[i] == '+') {
      bs.set(i);
    }
  }
  int totalFlips = 0;
  for (int i=0;i<L-K+1;++i) {
    if (bs[i]) {
      continue;
    }
    for (int j=i;j<i+K;++j) {
      bs.flip(j);
    }
    ++totalFlips;
  }
  for (int i=L-K+1;i<L;++i) {
    if (!bs[i]) {
      return -1;
    }
  }
  return totalFlips;
}

int main() {
  std::ifstream fin {"A-large.in"};
  std::ofstream fout {"A-large.out"};
  int T;
  fin >> T;
  for (int i=1;i<=T;++i) {
    std::string S;
    int K;
    fin >> S >> K;

    int minFlips = computeMinFlips(S, K);
    if (minFlips == -1) {
      fout << "Case #" << i << ": " << "IMPOSSIBLE" << std::endl;
    } else {
      fout << "Case #" << i << ": " << minFlips << std::endl;
    }
  }
  return 0;
}
