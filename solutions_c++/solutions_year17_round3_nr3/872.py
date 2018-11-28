#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

const ld EPS = 1e-13;
const int N = 55;

int t, T, n, k;
ld u, p[N], l, r, ans;

bool slv(ld x) {
  ld sm = 0;
  for(int i=0; i<n; ++i) sm += max(0.0L, x-p[i]);
  return sm < u;
}

int main() {
  scanf("%d", &T);
  while(t++ < T) {
    scanf("%d%d%Lf", &n, &k, &u);
    for(int i=0; i<n; ++i) scanf("%Lf", p+i);

    l = 0 - EPS, r = 1 + EPS;
    while(r - l > EPS) {
      ld m = (l+r)/2;
      if (slv(m)) l = m;
      else r = m;
    }

    ans = 1;
    for(int i=0; i<n; ++i) ans *= max(l, p[i]);
    printf("Case #%d: %Lf\n", t, ans);
  }
  return 0;
}
