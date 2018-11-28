// 2017 Round 1B, Problem
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
  In D, N;
  double time = 0;
  for (int j = N; j--;) {
    In K, S;
    time = std::max(time, double(D-K)/S);
  }
  return D/time;
}

int main() {
  In T;
  std::cout.precision(10);
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": "
              << do_case()
              << std::endl;
  }
  return 0;
}
