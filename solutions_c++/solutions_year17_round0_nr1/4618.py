#include <iostream>
#include <vector>

int main(int argc, char *argv[]) {
  unsigned int T, K;
  std::cin >> T;
  std::string row;

  for (unsigned int t = 0; t < T; ++t) {
    std::cin >> row >> K;
    std::vector<char> rowV(row.begin(), row.end());
    // for (const auto &u : rowV) std::cout << u;
    // std::cout << std::endl;
    unsigned int i = 0;
    int gedreht = 0;
    while (i < (rowV.size() - K)) {
      if (rowV[i] == '-') {
        ++gedreht;
        for (unsigned int d = i; d < (i + K); ++d) {
          if (rowV[d] == '-')
            rowV[d] = '+';
          else
            rowV[d] = '-';
        }
      }
      //      for (const auto &u : rowV) std::cout << u;
      //      std::cout << std::endl;
      ++i;
    }
    unsigned int allPlus = 0;
    unsigned int allMinus = 0;
    for (unsigned int d = i; d < rowV.size(); ++d) {
      if (rowV[d] == '-') ++allMinus;
      if (rowV[d] == '+') ++allPlus;
    }
    std::cout << "Case #" << t + 1 << ": ";
    if (allPlus > 0 and allMinus == 0) {
      std::cout << gedreht;
    } else if (allPlus == 0 and allMinus > 0) {
      std::cout << gedreht + 1;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
  return 0;
}
