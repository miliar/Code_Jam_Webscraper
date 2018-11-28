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

enum C {
  R,
  O,
  Y,
  G,
  B,
  V
};

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n;
    cin >> n;
    vector<int> c(6);
    for (int i = 0; i < 6; ++i) {
      cin >> c[i];
    }
    if (!(c[R] + c[Y] >= c[B] &&
        c[R] + c[B] >= c[Y] &&
        c[Y] + c[B] >= c[R])) {
      cout << "Case #" << t << ": IMPOSSIBLE\n";
      continue;
    }
    vector<string> res(3);
    for (int i = 0; i < c[R]; ++i) {
      res[0].push_back('R');
    }
    for (int i = 0; i < c[B]; ++i) {
      res[1].push_back('B');
    }
    for (int i = 0; i < c[Y]; ++i) {
      res[2].push_back('Y');
    }
    sort(res.begin(), res.end(), [] (string& a, string& b) { return a.size() < b.size(); });
    string fs;
    for (int i = 0; i < min(res[0].size(), res[1].size()); ++i) {
      fs.push_back(res[1][i]);
      fs.push_back(res[0][i]);
    }
    for (int i = min(res[0].size(), res[1].size()); i < max(res[0].size(), res[1].size()); ++i) {
      fs.push_back(res[1][i]);
    }
    reverse(fs.begin(), fs.end());
    string sc;
    for (int i = 0; i < min(fs.size(), res[2].size()); ++i) {
      sc.push_back(res[2][i]);
      sc.push_back(fs[i]);
    }
    for (int i = min(fs.size(), res[2].size()); i < max(fs.size(), res[2].size()); ++i) {
      sc.push_back(fs[i]);
    }
    cout << "Case #" << t << ": " << sc << '\n';
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
