#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pi;
vector< pi > v;

const int N = 1005;
bool vis[N][N];
ll memo[N][N];

ld PI = acos(-1);

ll side(int idx) {
  return 2 * v[idx].first * v[idx].second;
}

int T, n, k;
ll solve(int idx, int rem) {
  if (rem < 0) {
    return -(1LL << 61);
  }
  if (idx == v.size()) {
    if (rem == 0) {
      return 0;
    }
    return -(1LL << 61);
  }
  if (vis[idx][rem]) {
    return memo[idx][rem];
  }
  vis[idx][rem] = true;
  ll& ret = memo[idx][rem];
  // take
  ll take = solve(idx + 1, rem - 1) + side(idx);
  if (rem == k) {
    ll rad = v[idx].first;
    take += rad * rad;
  }
  // leave
  ll leave = solve(idx + 1, rem);
  return ret = max(take, leave);
}


int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> n >> k;
    v.clear();
    memset(vis, false, sizeof vis);
    int r, h;
    for (int i = 0; i < n; i++) {
      cin >> r >> h;
      v.push_back(pi(r, h));
    }
    sort(v.begin(), v.end(), greater<pi>());
    cout << "Case #" << tt << ": ";
    cout << fixed << setprecision(10) << solve(0, k) * PI << endl;
  }

  return 0;
}
