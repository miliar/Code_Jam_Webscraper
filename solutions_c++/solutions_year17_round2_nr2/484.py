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
const int N = 1005;

char ans[N];

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
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    int m = n / 2;
    vector<pair<int, char>> a = { {r,'R'},{y,'Y'},{b,'B'} };
    sort(a.begin(), a.end(), greater<pair<int, char>>());
    memset(ans, 0, sizeof(ans));
    if (a[0].first > m) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    ans[n] = 0;
    for (int i = 0; i < n; i += 2) {
      rep(j, 0, 2) {
        if (a[j].first > 0) {
          a[j].first--;
          ans[i] = a[j].second;
          break;
        }
      }
    }
    for (int i = 1; i < n; i += 2) {
      rep(j, 0, 2) {
        if (a[j].first > 0) {
          a[j].first--;
          ans[i] = a[j].second;
          break;
        }
      }
    }
    cout << ans << endl;
  }
  return 0;
}