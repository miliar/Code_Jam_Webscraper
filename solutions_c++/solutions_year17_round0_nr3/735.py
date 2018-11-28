#include <cstdio>
#include <algorithm>

using namespace std;

#define ll long long
#define pii pair<ll, ll>

const int N = 1e6 + 10;

ll n,k;
pii q[N];

inline void solve () {
  scanf ("%lld %lld", &n, &k);
  int f = 0,r = -1;
  q[++ r] = pii (n, 1);

  while (k > q[f].second) {
    pii a = pii (q[f].first / 2, q[f].second);
    if (f < r and q[r].first == a.first) {
      q[r].second += a.second;
    } else {
      q[++ r] = a;
    }
    a = pii ((q[f].first - 1) / 2, q[f].second);
    if (f < r and q[r].first == a.first) {
      q[r].second += a.second;
    } else {
      q[++ r] = a;
    }
    k -= q[f].second;
    f ++;
  }
  printf ("%lld %lld\n", q[f].first / 2, (q[f].first - 1) / 2);
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: ", i);
    solve ();
  }
}
