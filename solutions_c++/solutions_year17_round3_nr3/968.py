#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>

std::string solve(int k, double u, std::vector<double>& p);

int main() {
    int T = 0;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
      int n,k;
      std::cin >> n >> k;
      double u;
      std:: cin >> u;
      std::vector<double> p;
      for (int i=0; i<n; ++i) {
        double d;
        std::cin >> d;
        p.push_back(d);
      }

      std::cout << "Case #" << t << ": " << solve(k, u, p) << std::endl;
    }
    return 0;
}

std::string solve(int k, double u, std::vector<double>& p) {

  while (p.front() < 1.0 && u > 0.0) {
//    std::clog << "u: " << u << " front: " << p.front() << std::endl;
    std::sort(p.begin(), p.end());

    int same = 1;
    double prev = p.front();
    auto next = p.end();
    for (auto it = p.begin() + 1; it != p.end(); ++it) {
      next = it;
      if (prev != *it) break;
      ++same;
    }

  //  std::clog << "same: " << same << std::endl;

    double nextV = (next != p.end() && *next > prev) ? *next : 1.0;

    double diff = nextV - p.front();
    double take = same * diff;
    if (take > u) {
      take = u;
      diff = take / same;
    }

    for (int i=0; i<same; ++i) {
      p[i] += diff;
    }

    u -= take;
  }
  
  double prod = 1.0;
  for (const auto& pr : p) {
    prod *= pr;
  }

  std::stringstream out;
  out << std::fixed << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << prod;

  return out.str();
}
 
