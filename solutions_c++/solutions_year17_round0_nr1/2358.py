#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cassert>
using namespace std;

#define sz(a) int((a).size())
#define rep(i, s, n)  for(int i = s; i <= (n); ++i)
#define rev(i, n, s)  for(int i = (n); i >= s; --i)
#define fore(x, a) for(auto &&x : a)
typedef long long ll;
const int mod = 1000000007;
const int N = 100005;


int main() {
#ifdef loc
  if(!freopen((string(FOLDER) + "inp.txt").c_str(), "r", stdin)) {
    assert(0);
  }
  freopen((string(FOLDER) + "out.txt").c_str(), "w", stdout);
#endif
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t;
  cin >> t;
  rep(z, 1, t) {
    cout << "Case #" << z << ": ";
    string s;
    int k;
    cin >> s >> k;
    int n = sz(s);
    bool can = true;
    int res = 0;
    rep(i, 0, n - k) {
      if (s[i] == '-') {
        res++;
        rep(j, i, i + k - 1) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }
    rep(i, n - k + 1, n - 1) {
      if (s[i] == '-') can = false;
    }
    if (can) cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}