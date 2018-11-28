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

using namespace std;

#define f first
#define s second
#define pb push_back
#define pp pop_back
#define mp make_pair
#define ll long long
#define ld long double
#define ull unsigned long long
#define PI pair < int, int > 

const int N = 1234;
const ld Pi = acos(-1);
const ll Inf = 1e18;
const int inf = 1e2;
const int mod = 1e9 + 7;
const ld eps = 1e-12;

void add(int &a, int b) {
  a += b;
  if (a >= mod) a -= mod;
}
int mult(int a, int b) {
  return 1ll * a * b % mod;
}
int sum(int a, int b) {
  add(a, b);
  return a;
}

int id, t, n, c, m;
pair < int, int > a[N];
int f[N], ok[N], used[N], was[N][N], lst[N];

int get(int x) {
  int ans = 0;
  for (int i = x;i > 0;i = (i & (i + 1)) - 1) ans += f[i];
  return ans;
}
void upd(int x) {
  for (int i = x;i <= n;i = (i | (i + 1))) f[i]++;
} 
bool check(int x) {
  for (int i = 1;i <= m;i++) ok[i] = 0;
  for (int it = 0;it < x;it++) {
    for (int i = 1;i <= n;i++) f[i] = 0;
    for (int i = 1;i <= c;i++) used[i] = 0;
    for (int i = 1;i <= m;i++) {
      if (!ok[i] && !used[a[i].s]) {
        if (get(a[i].f) < a[i].f) {
          ok[i] = 1;
          used[a[i].s] = 1;
          upd(a[i].f);
        }
      }
    }
  }
  for (int i = 1;i <= m;i++) {
    if (!ok[i]) return 0;
  }
  return 1;
}
int fuck(int x) {
  int ans = m;
  memset(was, 0, sizeof was);
  for (int i = 1;i <= m;i++) lst[i] = -1;
  for (int i = 1;i <= m;i++) {
    for (int j = 1;j <= x;j++) {
      if (!was[j][i] && lst[j] < a[i].f) {
        lst[j] = a[i].f;
        ans--;
        was[j][i] = 1;
        break;
      }
    }
  }
  return ans;
}
void solve() {
  id++;
  cin >> n >> c >> m;
  for (int i = 1;i <= m;i++) {
    cin >> a[i].f >> a[i].s;
  }
  sort(a + 1, a + m + 1);
  int l = 1, r = m, ans = 0;
  while(l <= r) {
    int mid = (l + r) / 2;
    if (check(mid)) {
      ans = mid;
      r = mid - 1;
    } else l = mid + 1;
  }
  cout << "Case #" << id << ": " << ans << " " << fuck(ans) << endl;
}
int main() {
  #ifdef wws
    freopen("in", "r", stdin);
    freopen("out", "w", stdout); 
  #endif 
  ios_base::sync_with_stdio(0);
  cin >> t;
  while(t--) solve();
  return 0; 
}