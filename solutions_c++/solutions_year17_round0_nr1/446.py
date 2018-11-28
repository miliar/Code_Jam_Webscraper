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
    printf("Case #%d: ", test);
    string s;
    int k;
    cin >> s >> k;
    vi v(s.size());
    for (int i = 0; i < s.size(); ++i) if (s[i] == '-') v[i] = 1;
    int res = 0, sum = 0;
    vi add(s.size() + 1);
    for (int i = 0; i < s.size(); ++i) {
      sum ^= add[i];
      if (v[i] ^ sum) {
        if (i + k <= s.size()) {
          ++res;
          sum ^= 1;
          add[i + k] = 1;
          //for (int j = i; j < i + k; ++j) s[j] = s[j] == '-' ? '+' : '-';
        } else {
          res = -1;
          break;
        }
      }
    }
    if (res == -1) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << res << endl;
    }
  }
  return 0;
}
