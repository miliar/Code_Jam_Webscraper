// 2017 Round 1C, Problem
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


class In {                      // const long, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator long() {return i_;}
private:
  long i_;
};

static double do_case() {
  const double pi = 3.14159265358979;
  In N, K;
  std::vector<std::pair<int,int> > cake(N);
  for (auto &p : cake) std::cin >> p.first >> p.second;
  std::sort(cake.begin(), cake.end());
  const int l = N-K;
  
  std::vector<long>a(l+1);
  for (int i = 1; i <= K; ++i) {
    long prev = 0;
    for (int j=0; j <=l; ++j) {
      auto p = cake[N-i-j];
      const long area = p.first * (p.first*(i==1) + 2L * p.second);
      prev = a[j] = std::max(prev, area+a[j]);
    }
  }
  return pi*a[l];
}

int main() {
  std::cout.precision(10);
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": "
              << do_case()
              << std::endl;
  }
  return 0;
}
