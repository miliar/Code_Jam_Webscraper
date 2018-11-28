#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <numeric>
#include <limits>
#include <iomanip>

struct Pancake {
  double height;
  double radius;
  double givesOnSide;
  double givesOnTop;
  double gives;

  Pancake(int h, int r) : height(h), radius(r),
    givesOnSide(2 * height * radius), givesOnTop(radius * radius),
    gives(givesOnTop + givesOnSide){}

  Pancake& operator=(const Pancake&) = default;

  
  bool operator<(const Pancake& rhs) const {
    return givesOnSide < rhs.givesOnSide || (givesOnSide == rhs.givesOnSide && givesOnTop < rhs.givesOnTop);
  }
  
  //bool operator<(const Pancake& rhs) const {
  //  return gives < rhs.gives;
  //}

  void update(double maxR) {
    if (maxR > radius) {
      givesOnTop = 0;
      gives = givesOnSide;
    }
  }
};

using PancakeSet = std::vector<Pancake>;

std::string solve(int k, PancakeSet& set);

int main() {
    int T = 0;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        int n, k;
        std::cin >> n >> k;
        PancakeSet set;
        for (int i=0; i<n; ++i) {
          int r,h;
          std::cin >> r >> h;
          set.push_back(Pancake(h,r));
        }

        std::cout << "Case #" << t << ": " << solve(k, set) << std::endl;
    }
    return 0;
}

std::string solve(int k, PancakeSet& set) {
  std::sort(set.begin(), set.end());
//*
  for (const auto& p : set) {
    std::clog << p.height << ", " << p.radius << " | "
      << p.givesOnTop << " | " << p.givesOnSide<< " = " << M_PI*(p.givesOnTop + p.givesOnSide) << std::endl;
  }
//*/
  PancakeSet chosen;

  double sum = 0.0;
  double maxRad = 0.0; 
  for (int i=0; i<k; ++i) {
    auto p = set.back();
    auto it = &p;
    set.pop_back();
    chosen.push_back(p);

    if (it->radius > maxRad) maxRad = it->radius;
  }

  double maxWillAdd = 0.0;
  Pancake candidate(0,0);
  for (const auto& p : set) {
    if (p.radius > maxRad) {
      double willAdd = p.givesOnTop - pow(maxRad, 2);
      if (willAdd > maxWillAdd) {
        maxWillAdd = willAdd;
        candidate = p;
      }
    }
  }
  std::clog << "max will add " << maxWillAdd << std::endl;
  double minSwap = maxWillAdd + candidate.givesOnSide;
  int swi = -1;
  for (int i=0; i<k; ++i) {
    if (chosen[i].givesOnSide < (maxWillAdd + candidate.givesOnSide)) {
      if (chosen[i].givesOnSide < minSwap) {
        swi = i;
        minSwap = chosen[i].givesOnSide;
      }
    }
  }
  if (swi != -1) {
    maxRad = candidate.radius;
    std::swap(candidate, chosen[swi]);
  }

  for (int i=0; i<k; ++i) {
    sum += chosen[i].givesOnSide;
  }

  sum += pow(maxRad,2);
  sum *= M_PI;

  std::stringstream out;
  out << std::fixed << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << sum;

  return out.str();
}
 
