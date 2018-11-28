/**
 * jerry
 * C.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;
typedef pair<int, lli> pil;
typedef pair<lli, int> pli;
typedef pair<lli, lli> pll;

int gInt () {
  int i;
  scanf("%d", &i);
  return i;
}

lli gLong () {
  lli i;
  scanf("%lld", &i);
  return i;
}

double gDouble () {
  double i;
  scanf("%lf", &i);
  return i;
}

void quit () {
  fflush(stdout);
  exit(0);
}

lli n, k;

struct phash {
  size_t operator()(const pair<lli, lli>& p) const {
    return p.first * 1000007 + p.second;
  }
};

unordered_map<pair<lli, lli>, lli, phash> dp;

lli rec(lli n, lli k) {
  if (k == 0) {
    return (1LL << 61);
  }
  if (k == 1) {
    return n - 1;
  }
  pair<lli, lli> ind = make_pair(n, k);
  auto it = dp.find(ind);
  if (it != dp.end()) {
    return it->second;
  }

  lli ans = n - 1;
  lli a = (n - 1) >> 1, b = (n) >> 1;
  if (a == b) {
    ans = min(ans, rec(a, (k) >> 1));
    ans = min(ans, rec(b, (k - 1) >> 1));
  } else {
    ans = min(ans, rec(a, (k - 1) >> 1));
    ans = min(ans, rec(b, (k) >> 1));
  }
  fprintf(stderr, "%lld %lld: %lld\n", n, k, ans);
  return dp[ind] = ans;
}

pair<lli, lli> solve() {
  n = gLong();
  k = gLong();
  dp.clear();
  lli ans = rec(n, k);
  return make_pair((ans + 1) >> 1, ans >> 1);
}

int main (int argc, char ** argv) {
  int nC = gInt();
  for (int i = 0; i < nC; ++i) {
    pair<lli, lli> ans = solve();
    printf("Case #%d: %lld %lld\n", i + 1, ans.first, ans.second);
  }
  quit();
}
