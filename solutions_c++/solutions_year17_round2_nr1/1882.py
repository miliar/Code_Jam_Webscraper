#include <iostream>
#include <iomanip>
#include <cstdio>
#include <inttypes.h>

#include <string>
#include <vector>
#include <map>
#include <set>

#include <cmath>
#include <algorithm>

#include <cassert>

using namespace std;

double solve(uint64_t D, uint64_t N) {
  double maxT = 0;
  for (uint64_t i = 0; i < N; ++i) {
    uint64_t d, s; cin >> d >> s;
    double v = ((double)(D - d)) / ((double)s);
    if (v > maxT) maxT = v;
  }
  return ((double)D) / maxT;
}

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    uint64_t D, N; cin >> D >> N;
    printf("Case #%d: %.9f\n", i, solve(D, N));
  }
  return 0;
}
