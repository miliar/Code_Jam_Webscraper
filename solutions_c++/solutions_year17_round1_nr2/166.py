/**
 * jerry
 * B.cpp
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

struct intvl {
  int ingred;
  int ub;
};

int n, p;
int r[55];
int q[55][55];
int lb[55][55];
int ub[55][55];
map<int, vector<intvl>> intvls;
priority_queue<int> pqs[55];

int solve() {
  n = gInt();
  p = gInt();
  for (int i = 0; i < n; ++i) {
    r[i] = gInt();
  }
  intvls.clear();
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j) {
      q[i][j] = gInt();
      lb[i][j] = (q[i][j] * 10 + 11 * r[i] - 1) / (11 * r[i]);  // round up
      ub[i][j] = q[i][j] * 10 / (9 * r[i]);  // round down
      if (lb[i][j] <= ub[i][j]) {
//        fprintf(stderr, " add %d %d %d\n", i, lb[i][j], ub[i][j]);
        intvls[lb[i][j]].push_back({i, ub[i][j]});
      }
//      fprintf(stderr, "%d %d %d %d %d\n", i, j, q[i][j], lb[i][j], ub[i][j]);
    }
    pqs[i] = priority_queue<int>();
  }

  int ans = 0;
  for (const auto& elem : intvls) {
    int u = elem.first;
//    fprintf(stderr, "%d %lu\n", u, elem.second.size());
    for (const auto& intvl : elem.second) {
      pqs[intvl.ingred].push(-intvl.ub);
    }

    bool works = true;
    while (works) {
      for (int i = 0; i < n; ++i) {
        while (!pqs[i].empty() && -pqs[i].top() < u) {
          pqs[i].pop();
        }
        if (pqs[i].empty()) {
          works = false;
        }
      }

      if (works) {
        ++ans;
        for (int i = 0; i < n; ++i) {
          pqs[i].pop();
        }
      }
    }
  }

  return ans;
}

int main (int argc, char ** argv) {
  int t = gInt();
  for (int i = 0; i < t; ++i) {
    fprintf(stderr, "case %d\n", i + 1);
    printf("Case #%d: %d\n", i + 1, solve());
  }
  quit();
}
