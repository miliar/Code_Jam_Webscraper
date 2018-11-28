#include <bits/stdc++.h>

using namespace std;

int T, cs;

int main()
{
  freopen("A-large (1).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    printf("Case #%d: ", ++cs);
    double mx = 0;
    int n, d, k, s;
    scanf("%d %d", &d, &n);
    while(n--){
      scanf("%d %d", &k, &s);
      mx = max(mx, (double)(d - k)/s);
    }
    printf("%.6lf\n", d / mx);
  }
  return 0;
}
