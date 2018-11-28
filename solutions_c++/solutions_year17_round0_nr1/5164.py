/**
 * jerry
 * A.cpp
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

char buf[100005];
int k;
int n;

void flip(int i) {
  if (buf[i] == '-') {
    buf[i] = '+';
  } else {
    buf[i] = '-';
  }
}

int solve() {
  scanf("%s", buf);
  k = gInt();
  n = strlen(buf);
  int ans = 0;
  for (int i = 0; i <= n - k; ++i) {
    if (buf[i] == '-') {
      for (int j = 0; j < k; ++j) {
        flip(i + j);
      }
      ++ans;
    }
  }
  for (int i = 0; i < n; ++i) {
    if (buf[i] == '-') {
      return -1;
    }
  }
  return ans;
}

int main (int argc, char ** argv) {
  int nC = gInt();
  for (int i = 0; i < nC; ++i) {
    int ans = solve();
    printf("Case #%d: ", i + 1);
    if (ans < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
  quit();
}
