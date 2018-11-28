#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

const ld PI = acos(-1);
const int N = 1000;
int n, k, t, T, r[N], x[N], h[N], rx, hx, id[N];
ld ans;

bool cp(int i, int j) { return r[i] > r[j]; }

bool cp2(int i, int j) { return 1ll*h[i]*r[i] > 1ll*h[j]*r[j]; }

int main() {
  scanf("%d", &T);
  while(t++ < T) {
    ans = 0;
    scanf("%d%d", &n, &k);

    for(int i=0; i<n; ++i) {
      scanf("%d%d", r+i, h+i);
      id[i] = i;
    }

    sort(id, id+n, cp);
    for(int i=0; i<n; ++i) x[i] = r[id[i]];
    for(int i=0; i<n; ++i) r[i] = x[i];

    for(int i=0; i<n; ++i) x[i] = h[id[i]];
    for(int i=0; i<n; ++i) h[i] = x[i];

    for(int i=0; i<n; ++i) {
      ld area = 2*PI*r[i]*h[i] + PI*r[i]*r[i];
      int c = 1;
      sort(id, id+n, cp2);

      for(int j=0; j<n and c<k; ++j) if (id[j] > i) {
        area += 2*PI*r[id[j]]*h[id[j]];
        c++;
      }

      ans = max(ans, area);
    }

    printf("Case #%d: %.15Lf\n", t, ans);
  }
  return 0;
}
