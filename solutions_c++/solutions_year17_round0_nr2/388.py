// Qualification Round 2017, Problem B.  
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

static void do_case() {
  In N;
  short neat[19], length = 0;
  for (long n = N; n > 0; n /= 10) {
    int digit = n % 10;
    if (length && digit > neat[length-1]) {
      std::fill_n(neat, length, 9);
      --digit;
    }
    neat[length++] = digit;     // might be zero
  }
  length -= !neat[length-1];    // omit leading zero.  Can only have 1
  while (length--) std::cout << neat[length];
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": ";
    do_case();
    std::cout << std::endl;
  }
  return 0;
}
