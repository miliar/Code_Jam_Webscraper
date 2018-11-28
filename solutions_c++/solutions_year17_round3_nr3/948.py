// 2017 Round 1C, Problem
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


template <class T>
class In {                      // const long, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator T() {return i_;}
private:
  T i_;
};

static double do_case() {
  In<int>N, K;
  In<double>U;
  std::vector<double> p(N);
  for (double &pp : p) std::cin >> pp;
  p.push_back(100);            // sentinel
  std::sort(p.begin(), p.end());
  double sum = 0, s1;
  int train = 1;
  while (sum + (s1 = train * (p[train]-p[train-1])) < U) {
    sum += s1;
    ++train;
  }
  const double level = p[train-1] + (U-sum) / train;
  std::cerr << "train " << train << " cores to level " << level << std::endl;
  double best = pow(level, train);
  for (int j = train; j < N; ++j)
    best *= p[j];
  return best;
}

int main() {
  std::cout.precision(10);
  In<int> T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": "
              << do_case()
              << std::endl;
  }
  return 0;
}
