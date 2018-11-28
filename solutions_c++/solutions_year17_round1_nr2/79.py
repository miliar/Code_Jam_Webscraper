/*
  by Nazarbek Altybay
  nazarbek.altybay@gmail.com
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

#define f first
#define s second

#define pb push_back
#define mp make_pair

using namespace std;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

int n, m;
int need[N];
int a[55][55];

void solve() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++)
    scanf("%d", &need[i]);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      scanf("%d", &a[i][j]);
    }
    sort(a[i] + 1, a[i] + m + 1);
  }
  int maxval = *max_element(need + 1, need + n + 1);
  long long old = 0, ans = 0;
  for (int cnt = 1; cnt <= (int) 1e6; cnt++) {
    long long prod = 1;
    if ((maxval * 1ll * cnt * 9 + 9) / 10 > (long long)1e6)
      break;
    vector<int> id;
    for (int i = 1; i <= n; i++) {
      long long l = (need[i] * 1ll * cnt * 9 + 9) / 10;
      long long r = (need[i] * 1ll * cnt * 11) / 10;
      int here = 0;
      for (int j = 1; j <= m; j++)
        if ((long long) a[i][j] >= l && (long long) a[i][j] <= r) {
          id.pb(j);
          break;
        }
    }
    if ((int) id.size() == n) {
      for (int i = 1; i <= n; i++)
        a[i][id[i - 1]] = 0;
      ans++;
      cnt--;
    }
  }
  cout << ans << endl;
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; cases++) {
    printf("Case #%d: ", cases);
    //prepare();
    solve();
    cerr << cases << "done\n";
  }

  return 0;
}