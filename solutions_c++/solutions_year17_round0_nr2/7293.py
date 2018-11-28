#include "gcj.h"

int main(int argc, char* argv[]) {
  std::ifstream ifs(argv[1]);
  if(!ifs.good()) {
    return 1;
  }
  std::ofstream ofs((argc >= 3) ? std::ofstream(argv[2]) : std::ofstream());

  const std::vector<std::string> testCases(GCJ::getTestCases(ifs));
  for(size_t t = 0; t < testCases.size(); ++t) {
    std::string n(testCases[t]);

    bool tidy = (1 == n.size());
    while(!tidy && (n.size() >= 2)) {
      const int64_t currentN = std::stoll(n);

      for(size_t i = n.size() - 1; i > 0; --i) {
        const int32_t digitLow = n[i] - '0';
        const int32_t digitHigh = n[i - 1] - '0';

        if(digitLow < digitHigh) {
          const int64_t newHigh = std::stoll(n.substr(0, i)) - 1;
          const std::string newHighStr((newHigh >= 1) ? std::to_string(newHigh) : "");
          const std::string newLowStr(n.size() - i, '9');
          n = newHighStr + newLowStr;
          break;
        }
      }

      if(currentN == std::stoll(n)) {
        tidy = true;
      }
    }

    std::string output(GCJ::casePrefix(t + 1) + n);

    if(ofs.is_open()) {
      ofs << output << std::endl;
    } else {
      std::cout << output << std::endl;
    }
  }

  return 0;
}
