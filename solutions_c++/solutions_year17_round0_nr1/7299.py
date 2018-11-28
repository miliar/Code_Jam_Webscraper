#include "gcj.h"

int main(int argc, char* argv[]) {
  std::ifstream ifs(argv[1]);
  if(!ifs.good()) {
    return 1;
  }
  std::ofstream ofs((argc >= 3) ? std::ofstream(argv[2]) : std::ofstream());

  int32_t numberOfTestCases = GCJ::getNumberOfTestCases(ifs);
  for(size_t t = 1; t <= numberOfTestCases; ++t) {
    std::string s;
    uint32_t k = 0;
    ifs >> s >> k;

    int32_t flips = 0;
    bool impossible = false;
    for(size_t i = 0; i < s.size(); ++i) {
      if(s[i] == '-') {
        if((i + k) > s.size()) {
          impossible = true;
        } else {
          ++flips;
          for(size_t f = i; f < (i + k); ++f) {
            s[f] = (s[f] == '-') ? '+' : '-';
          }
        }
      }
    }

    std::string output(GCJ::casePrefix(t));
    output += (impossible) ? "IMPOSSIBLE" : std::to_string(flips);

    if(ofs.is_open()) {
      ofs << output << std::endl;
    } else {
      std::cout << output << std::endl;
    }
  }

  return 0;
}
