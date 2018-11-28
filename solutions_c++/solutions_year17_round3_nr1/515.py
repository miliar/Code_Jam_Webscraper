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

long double pi = acosl(-1);
int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n, k;
    cin >> n >> k;
    vector<long double> r(n);
    vector<long double> h(n);
    for (int i = 0; i < n; ++i) {
      cin >> r[i] >> h[i];
    }
    long double result = 0;
    for (int i = 0; i < n; ++i) {
      long double cur = 2 * pi * r[i] * h[i];
      vector<long double> hs;
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        if (r[j] <= r[i]) {
          hs.push_back(2 * pi * r[j] * h[j]);
        }
      }
      sort(hs.begin(), hs.end(), std::greater<long double>());
      for (int c = 0; c < min((int) hs.size(), k - 1); ++c) {
        cur += hs[c];

      }
      result = max(result, cur + pi * r[i] * r[i]);
    }
    cout << fixed << setprecision(10);
    cout << "Case #" << t << ": ";
    cout << double(result) << '\n';
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
