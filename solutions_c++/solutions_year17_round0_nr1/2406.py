#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;



void Solve() {
  std::string str;
  cin >> str;
  int k, n;
  n = str.size();
  cin >> k;
  int ret = 0;
  for (int i = 0; i <= n - k; ++i) {
    if (str[i] == '-') {
      ++ret;
      for (int j = 0; j < k; ++j) {
        if (str[i + j] == '-') {
          str[i + j] = '+';
        } else {
          str[i + j] = '-';
        }
      }
    }
  }
  bool failed = false;
  for (int i = 0; i < n; ++i) {
    if (str[i] == '-') {
      failed = true;
    }
  }
  if (failed) {
    puts("IMPOSSIBLE");
  } else {
    printf("%d\n", ret);
  }
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
