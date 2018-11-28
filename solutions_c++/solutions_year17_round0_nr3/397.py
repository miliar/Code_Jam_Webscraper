// Qualification Round 2017, Problem C.  Bathroom Stalls
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <map>
#include <algorithm>


class In {                      // const int, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator int() {return i_;}
private:
  int i_;
};


static int do_case() {
  In N, K;
  std::map<int,int> gap;
  gap[N] = 1;
  int min, max;
  for (int k = K; k>0;) {
    std::pair<int,int> big = *gap.rbegin();
    max = big.first/2;
    min = (big.first-1)/2;
    k -= big.second;            // took care of big.second people
    gap[min] += big.second;
    gap[max] += big.second;
    gap.erase(big.first);
  }
  std::cout << max << " " << min << std::endl;
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": ";
    do_case();
  }
  return 0;
}
