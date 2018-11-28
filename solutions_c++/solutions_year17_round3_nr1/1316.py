#include <bits/stdc++.h>

#define fst first
#define snd second

using namespace std;

const int maxn = 1e6 + 5;
const double pi = acos(0.0) * 2.0;
int n, k;
struct pk {
  double r, h, ar;
}p[maxn];

bool cmp(pk a, pk b) {
  return a.ar > b.ar;
}

void solve() {
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; i++) {
    scanf("%lf%lf", &p[i].r, &p[i].h);
    p[i].ar = 2 * pi * p[i].r * p[i].h;
  }
  sort(p, p + n, cmp);
  double tot = 0, maxr = 0;
  for (int i = 0; i < k - 1; i++) {
    maxr = max(maxr, p[i].r);
    tot += p[i].ar;
  }
  double maxx = 0;
  for (int i = k - 1; i < n; i++) {
    double tmp = max(maxr, p[i].r);
    maxx = max(tmp * tmp * pi + p[i].ar, maxx);
  }
  tot += maxx;
  printf("%f\n", tot);
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("kida.out", "w", stdout);
  int t; scanf("%d", &t);
  for (int Case = 1; Case <= t; Case++) {
    printf("Case #%d: ", Case);
    solve();
  }
  return 0;
}
