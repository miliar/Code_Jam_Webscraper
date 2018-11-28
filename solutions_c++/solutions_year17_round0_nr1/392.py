// Qualification Round 2017, Problem A.  
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <string>


class In {                      // const int, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator int() {return i_;}
private:
  int i_;
};

static void do_case() {
  std::string S;                // row of pancakes, mutable
  std::cin >> S;
  In K;                         // flipper width
  const int w = S.size();     // shorthand
  static const char flip = '+' ^ '-'; // 6
  int count = 0;
  for (int j = 0; j < w; ++j)
    if (S[j] == '-') {
      if (j + K > w) {
        std::cout << "IMPOSSIBLE" << std::endl;
        return;
      }
      ++count;
      for (int k = K; k--;) S[j+k] ^= flip;
    }
  std::cout << count << std::endl;
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": ";
    do_case();
  }
  return 0;
}
