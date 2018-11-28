#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int val(int t) {
  if (t < 0) return 0;
  if (t >= 2) return 2;
  return 1;
}

void add(int i, int j, int t, vvi & v, vector<array<int, 3>> & res, int & sum) {
  sum += val(t) - val(v[i][j]);
  v[i][j] = t;
  res.push_back({t, i, j});
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    int n, m;
    cin >> n >> m;
    int sum = 0;
    vector<array<int, 3>> res;
    int col = -1, col1 = -1;
    vvi a(n, vi(n, -1));
    for (int i = 0; i < m; ++i) {
      string s;
      int t, x, y;
      cin >> s >> x >> y;
      --x; --y;
      if (s == "+") t = 0;
      if (s == "x") t = 1;
      if (s == "o") t = 2;
      sum += val(t);
      a[x][y] = t;
      if (t == 1) {
        add(x, y, 2, a, res, sum);
      }
      if (a[x][y] == 2) col = y;
    }
    if (col == -1) {
      add(0, 0, 2, a, res, sum);
      col = 0;
    }
//    cerr << col << endl;
    for (int j = 0; j < n; ++j) if (a[0][j] == -1) {
      add(0, j, 0, a, res, sum);
    }
    for (int j = 1; j + 1 < n; ++j) {
      if (j == col || col1 != -1) {
        add(n-1, j, 0, a, res, sum);
      } else {
        add(n-1, j, 2, a, res, sum);
        col1 = j;
      }
    }
//    cerr << col << ' ' << col1 << endl;
    int j = 0;
    for (int i = 1; i < (col1 != -1 ? n-1 : n); ++i, ++j) {
      while (j == col || j == col1) ++j;
      add(i, j, 1, a, res, sum);
    }
    cout << sum << ' ' << res.size() << endl;
    for (int i = 0; i < res.size(); ++i) {
      char ch = '+';
      if (res[i][0] == 1) ch = 'x';
      if (res[i][0] == 2) ch = 'o';
      cout << ch << ' ' << res[i][1] + 1 << ' ' << res[i][2] + 1 << endl;
    }
  }
  return 0;
}
