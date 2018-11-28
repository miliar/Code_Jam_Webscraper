#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

const int MAXN = 1010;
const double pi = acos(-1);

class pancake {
  public:
    long long r, h, area;
};

pancake a[MAXN];

bool cmp(pancake a, pancake b) {
  return a.area > b.area;
}

int main() {
  freopen("Alarge.in", "r", stdin);
  freopen("Alarge.out", "w", stdout);
  long long T, n, m;
  long long sum, res, maxR;

  scanf("%lld", &T);
  rep(cas, 1, T + 1) {
    scanf("%lld%lld", &n, &m);
    rep(i, 0, n) {
      scanf("%lld%lld", &a[i].r, &a[i].h);
      a[i].area = 2 * a[i].r * a[i].h;
    }
    sort(a, a + n, cmp);
    res = 0;
    maxR = 0;
    rep(i, 0, m) {
      maxR = max(maxR, a[i].r);
      res += a[i].area;
    }
    res += maxR * maxR;
    
    sum = 0;
    rep(i, 0, m - 1) {
      sum += a[i].area;
    }
    rep(i, m, n) {
      res = max(res, sum + a[i].r * a[i].r + a[i].area);
    }
    printf("Case #%d: %.9lf\n", cas, pi * res);
  }

  return 0;
}
