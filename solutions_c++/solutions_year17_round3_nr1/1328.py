#include <bits/stdc++.h> 

using namespace std;

typedef long long ll;

#define x first
#define y second

const int N = 1005;
const long double PI = acos(-1.0);

int t, cs, n, k;
pair <ll, ll> p[N];

bool cmp (pair <ll, ll> a, pair <ll, ll> b) {
  ll tmp = a.x * a.y - b.x * b.y;
  if (tmp == 0) return a.x > b.x;
  return tmp > 0;
}

int main (int argc, char const *argv[]) {
  scanf("%d", &t); while (t--) {
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; ++i) {
      scanf("%lld %lld", &p[i].x, &p[i].y);
    }
    sort(p + 1, p + n + 1, cmp);
    ll maximum = 0, sum = 0;
    for (int i = 1; i < k; ++i) {
      maximum = max(maximum, p[i].x);
      sum += p[i].x * p[i].y;
    }
    ll res = 0;
    for (int i = k; i <= n; ++i) {
      ll cur = max(maximum, p[i].x);
      res = max(res, cur * cur + 2 * (sum + p[i].x * p[i].y));
    }
    long double ans = PI * res;
    printf("Case #%d: %0.12f\n", ++cs, (double) ans);
  }
  return 0;
}

