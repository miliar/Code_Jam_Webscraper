#include <bits/stdc++.h>
using namespace std;
typedef long long Long;
typedef long double LD;

const int N = 51;

LD p[N];
LD u;
int n, k;

bool Can(LD x) {
  LD needed = 0;
  for (int i = 0; i < n; ++i) {
    needed += max(LD(0), x - p[i]);
  }
  return needed <= u + 1e-9;
}

LD GetMinPos() {
  LD low = 0, high = 1, mid;

  for (int iter = 0; iter < 40; ++iter) {
    mid = (low + high) / 2;
    if (Can(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  return mid;
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

    cin >> n >> k;

    cin >> u;

    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }

    LD mn = GetMinPos();

    LD res = 1;
    for (int i = 0; i < n; ++i) {
      res *= max(p[i], mn);
    }

    cout << fixed << setprecision(10) << res << '\n';
  }
}
