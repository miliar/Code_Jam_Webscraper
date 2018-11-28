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

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d:\n", test);
    int n, m;
    cin >> n >> m;
    vs s(n);
    for (int i = 0; i < n; ++i) {
      cin >> s[i];
      for (int j = 1; j < m; ++j) {
        if (s[i][j-1] != '?' && s[i][j] == '?') s[i][j] = s[i][j-1];
      }
      for (int j = m-2; j >= 0; --j) {
        if (s[i][j+1] != '?' && s[i][j] == '?') s[i][j] = s[i][j+1];
      }
    }
    for (int i = 1; i < n; ++i) {
      if (s[i-1][0] != '?' && s[i][0] == '?') s[i] = s[i-1];
    }
    for (int i = n-2; i >= 0; --i) {
      if (s[i+1][0] != '?' && s[i][0] == '?') s[i] = s[i+1];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        assert(isalpha(s[i][j]));
      }
      cout << s[i] << endl;
    }
  }
  return 0;
}
