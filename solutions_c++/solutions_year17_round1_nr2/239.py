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

long long costs[1005];
long long vals[1005][1005];

std::pair<long long, long long> getServs(long long cost, long long mat) {
  long long minServ = (10 * mat) / (11 * cost);
  if (!minServ) {
    ++minServ;
  }
  while (minServ * cost * 11 < mat * 10) {
    ++minServ;
  }
  
  long long maxServ = (10 * mat) / (9 * cost) + 1;
  while (maxServ * cost * 9 > mat * 10) {
    --maxServ;
  }
  return make_pair(minServ, maxServ);
}

void Solve() {
  int n, p;
  cin >> n >> p;
  for (int i = 0; i < n; ++i) {
    cin >> costs[i];
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j) {
      cin >> vals[i][j];
    }
  }
  vector<vector<pair<long long, long long>>> v;
  v.resize(n);
  vector<int> pos(n, 0);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j) {
      auto x = getServs(costs[i], vals[i][j]);
      if (x.first > x.second) {
        continue;
      }
      v[i].push_back(x);
    }
    sort(v[i].begin(), v[i].end());
  }

  int ret = 0;
  while (true) {
    long long max_min = -1;
    for (int i = 0; i < n; ++i) {
      if (pos[i] == v[i].size()) {
        cout << ret << endl;
        return;
      }
      max_min = max(max_min, v[i][pos[i]].first);
    }
    bool skipped = false;
    for (int i = 0; i < n; ++i) {
      while (pos[i] < v[i].size() && v[i][pos[i]].second < max_min) {
        ++pos[i];
        skipped = true;
      }
    }
    if (skipped) {
      continue;
    }
    ++ret;
    for (int i = 0; i < n; ++i) {
      ++pos[i];
    }
  }
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
