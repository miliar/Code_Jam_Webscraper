#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <limits>
#include <algorithm>
#include <set>
#include <map>


struct Horse {
  int64_t start;
  int64_t velocity;

  bool operator<(const Horse& rhs) const{
    return start < rhs.start || (start == rhs.start && velocity < rhs.velocity);
  }
};

std::string solve(int64_t D, std::set<Horse>& horses);

int main() {
    int T = 0;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        int64_t D, N;
        std::cin >> D >> N;
        std::set<Horse> horses;
        for (int64_t j=0; j<N; ++j) {
          Horse h;
          std::cin >> h.start >> h.velocity;
          horses.insert(h);
        }

        std::cout << "Case #" << t << ": " << solve(D, horses) << std::endl;
    }
    return 0;
}

struct Cut {
  double when;
  double where;

  bool operator<(const Cut& rhs) const {
    return when < rhs.when || (when == rhs.when && where < rhs.where);
  }
};

Cut cut(const Horse& lhs, const Horse& rhs) {
  if (lhs.velocity == rhs.velocity) return Cut{-1.0,-1.0};

  double t = double(lhs.start - rhs.start) / double(rhs.velocity - lhs.velocity);

  return Cut{ t, lhs.start + t * lhs.velocity };
}

std::string solve(int64_t D, std::set<Horse>& horses) {
  auto cur = horses.begin();
  while (cur != horses.end()) {
    auto it = cur;
    std::map<Cut, decltype(it)> cuts;
    for (++it; it != horses.end(); ++it) {
      Cut c = cut(*cur, *it);
      if (c.when >= 0.0 && c.where <= double(D)) {
        cuts[c] = it; 
      }
    }

    if (!cuts.empty()) {
      // Cut c = cuts.begin()->first;
      Horse a = *cur;
      Horse b = *(cuts.begin()->second);

      Horse choice = (a.velocity < b.velocity) ? a : b;

      horses.erase(cur);
      horses.erase(cuts.begin()->second);

      horses.insert(choice);
      cur = horses.begin();
    } else {
      ++cur;
      break; // actually... this one is the slowest...
    }
  }

  Horse slowest = *horses.begin();
  double tCut = double(D - slowest.start) / slowest.velocity;

  double v = double(D) / tCut;

  std::stringstream out;
  out << std::fixed << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << v;

  return out.str();
}
 
