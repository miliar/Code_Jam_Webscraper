#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)

typedef long long ll;

const int N = 1e6;
int n, kk, lmin, lmax;
int s[N+2];

int main() {
  int tt;
  scanf("%d ", &tt);
  REP(t,tt) {
    scanf("%d%d ", &n, &kk);
    memset(s, 0, sizeof(s));
    s[0] = s[n+1] = 1;
    lmin = 0, lmax = N;
    REP(i,kk) {
      int idx = n;
      int lmin_tmp = 0, lmax_tmp = 0;
      REP(j,n) {
        if (s[n-j]) continue;
        int dl = n-j-1, dr = n-j+1;
        while (dl > 0 && !s[dl]) dl--;
        while (dr < n+1 && !s[dr]) dr++;
        dl = n-j - dl - 1;
        dr = dr - (n-j) - 1;
        if (lmin_tmp < min(dl,dr)) {
          lmin_tmp = min(dl,dr); 
          lmax_tmp = max(dl,dr); 
          idx = n-j;
        } else if (lmin_tmp == min(dl,dr) && lmax_tmp <= max(dl,dr)) {
          lmin_tmp = min(dl,dr); 
          lmax_tmp = max(dl,dr); 
          idx = n-j;
        } 
      } 
      s[idx] = 1;
      lmin = lmin_tmp, lmax = lmax_tmp;
    }
    printf("Case #%d: %d %d\n", t+1, lmax, lmin);
  }
  return 0;
}

