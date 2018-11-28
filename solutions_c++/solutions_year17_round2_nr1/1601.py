#include <bits/stdc++.h>
using namespace std;

int main() {
  int t=0, T, n, D;
  scanf("%d", &T);
  while(T--) {
    cin >> D >> n;
    printf("Case #%d: ", ++t);
    double tt;
    int x, y;
    for(int i=0;i<n;i++) {
      cin >> x >> y;
      double s = 1.0*(D-x)/y;
      tt = max(s, tt);
      if(i==0) tt = s;
    }
    printf("%.9lf\n", 1.0*D/tt);
  }
}
