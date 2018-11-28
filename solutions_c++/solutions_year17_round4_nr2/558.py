#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

const int N = 1e3 + 3;
const int OO = 1e9;

int cnt[N];
int cust[N];

int rides;
int Get(int ind, int rem) {
  if (ind == 0) {
    if (rem > 0) return OO;
    return 0;
  }

  int res = OO;
  int cost = max(0, cnt[ind] - rides);
  int av = max(0, rides - cnt[ind]);

  if (av > 0) {
    rem = max(0, rem - av);
  } else {
    rem += cnt[ind] - rides;
  }


  res = min(res, cost + Get(ind - 1, rem));
  return res;
}

int Solve() {
  int low = 1, high = 1e3 + 3, mid, ans = -1;
  for (int x : cust) {
    low = max(low, x);
  }
  while (low <= high) {
    mid = (low + high) / 2;
    rides = mid;

    int res = Get(N - 1, 0);
    if (res != OO) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";
    memset(cnt, 0, sizeof cnt);
    memset(cust, 0, sizeof cust);

    int n, c, m;
    cin >> n >> c >> m;

    while (m--) {
      int p, b;
      cin >> p >> b;
      ++cnt[p];
      ++cust[b];
    }

    int r = Solve();
    rides = r;
    cout << r << ' ' << Get(N - 1, 0) << '\n';
  }

}
