#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (const auto& el : vec) {
    fout << el << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n, q;
    cin >> n >> q;
    vector<int> e(n);
    vector<int> s(n);
    vector<int> d(n);
    for (int i = 0; i < n; ++i) {
      cin >> e[i];
      cin >> s[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        int dist;
        cin >> dist;
        if (i + 1 == j) {
          d[i] = dist;
        }
      }
    }
    for (int i = 0; i < q; ++i) {
      int buf;
      cin >> buf >> buf;
    }
    vector<double> dp(n, 1e34);
    dp[0] = 0;
    for (int i = 0; i < n; ++i) {
      double dist = 0;
      for (int j = i + 1; j < n; ++j) {
        dist += d[j - 1];
        if (dist > e[i]) break;
        dp[j] = min(dp[j], dp[i] + dist / s[i]);
      }
    }
    cout << fixed << setprecision(10) << "Case #" << t << ": " << dp[n - 1] << '\n';

  }

  return 0;
}


int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  //freopen("input.txt", "rt", stdin);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  Solve();
  return 0;
}
