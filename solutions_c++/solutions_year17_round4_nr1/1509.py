#include <bits/stdc++.h>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>

#define f first
#define s second

#define pb push_back
#define pp pop_back
#define mp make_pair

#define sz(x) (int)x.size()
#define sqr(x) ((x) * 1ll * (x))
#define all(x) x.begin(), x.end()

#define rep(i, l, r) for (int i = l; i <= r; i++)
#define per(i, l, r) for (int i = l; i >= r; i--)

#define dbg(x) cerr << (#x) << " --> " << (x) << nl;
#define Kazakhstan ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);

#define nl '\n'
#define ioi exit(0);

#define Toktama "A-small-attempt3"

using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef tree < pair <int, int>, null_type, less < pair <int, int> >, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const int N = (int)100 + 7, inf = (int)1e9 + 7, mod = (int)1e9 + 7;
const ll linf = (ll)1e18 + 7;
const int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1}, dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

int n, p, t;
int a[N];
bool was[N];

int calc(int x, int y) {
  int res = x;
  while (res < y)
    res += x;
  return res - y;
}
bool cmp(int x, int y) {
  int sol = calc(p, x), on = calc(p, y);
  return sol < on;
}
void solve(int id) {
  scanf ("%d%d", &n, &p);
  multiset <int> st;
  rep(i, 1, n)
    scanf ("%d", &a[i]);



  sort (a + 1, a + 1 + n, cmp);
  int res = 0;
  rep(z, 1, 5000) {
    int ans = 0, add = 0;
    rep(i, 1, n) {
      if (add >= a[i]) add -= a[i];
      else {
        if (add == 0) ans++;
        add = calc(p, a[i] - add);
      }
    }
    res = max(res, ans);
    random_shuffle(a + 1, a + 1 + n);
  }
  cout << "Case #" << id << ": " << res << nl;
}
int main() {
  #ifdef Toktama
    freopen (Toktama".in", "r", stdin);
    freopen (Toktama".out", "w", stdout);
  #endif
  scanf ("%d", &t);
  rep(i, 1, t)
    solve(i);
  ioi
}
