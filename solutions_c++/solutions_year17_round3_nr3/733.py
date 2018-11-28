#include <bits/stdc++.h>
using namespace std;

double p[55];

int main(){
  freopen("C-small-1-attempt0.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int qq = 1; qq <= t; qq++) {
    printf("Case #%d: ", qq);
    int n, k;
    scanf("%d %d",&n,&k);
    double u;
    scanf("%lf",&u);
    for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
    sort(p, p + n);
    int cur = -1;
    for (int i=1;i<n;i++){
      if(u < i * (p[i] - p[i-1])) {
        cur=i;
        break;
      }
      u -= i * (p[i] - p[i-1]);
      for (int j = 0; j < i; j++) {
        p[j] = p[i];
      }
    }
    if (cur == -1) {
      cur = n;
    }
    for (int i = 0; i < cur; i++){
      p[i] += (u / cur);
    }
    double ret = 1;
    for (int i = 0; i < n; i++) ret *= p[i];
    printf("%lf\n", ret);
  }
}
