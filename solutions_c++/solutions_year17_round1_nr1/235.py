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

string f[32];

void Solve() {
  for (int i = 0; i < 32; ++i) {
    f[i] = "";
  }
  int r, c;
  cin >> r >> c;
  for (int i = 0; i < r; ++i) {
    cin >> f[i];
  }
  for (int i = 0; i < r; ++i) {
    for (int j = 1; j < c; ++j) {
      if (f[i][j] == '?') {
        f[i][j] = f[i][j - 1];
      }
    }

    for (int j = c - 2; j > -1; --j) {
      if (f[i][j] == '?') {
        f[i][j] = f[i][j + 1];
      }
    }
  }
  for (int i = 1; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      if (f[i][j] == '?') {
        f[i][j] = f[i - 1][j];
      }
    }
  }
  for (int i = r - 2; i > -1; --i) {
    for (int j = 0; j < c; ++j) {
      if (f[i][j] == '?') {
        f[i][j] = f[i + 1][j];
      }
    }
  }

  for (int i = 0; i < r; ++i) {
    cout << f[i] << endl;
  }
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d:\n", i + 1);
        Solve();
    }
    return 0;
}
