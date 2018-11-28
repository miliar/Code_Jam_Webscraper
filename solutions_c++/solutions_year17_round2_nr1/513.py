#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void) {
  if (fopen("probAsmall.in", "r")) {
    freopen("probAsmall.in", "r", stdin);
    freopen("probAsmall.out", "w", stdout);
  }
  if (fopen("probAlarge.in", "r")) {
    freopen("probAlarge.in", "r", stdin);
    freopen("probAlarge.out", "w", stdout);
  }
  int t;
  scanf("%d", &t);
  for (int ii = 1; ii <=t; ii++) {
    double ans = 1e16;
    double d;
    int n;
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      double ki, si;
      cin >> ki >> si;
      ans = min(ans, (si * d) / (d - ki));
    }
    printf("Case #%d: %.9f\n", ii, ans);
  }
  return 0;
}
