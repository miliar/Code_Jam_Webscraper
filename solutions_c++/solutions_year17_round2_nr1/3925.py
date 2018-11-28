#include <iostream>
using namespace std;
int k[1001];
int s[1001];
double ti[1001];
int main() {
  int t, d, n;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cin >> d >> n;
    for(int i = 0; i < n; i++) {
      cin >> k[i] >> s[i];
    }
    ti[n-1] = (double)(d-k[n-1])/(double)s[n-1];
    for(int i = n-2; i >= 0; i--) {
      ti[i] = max((double)(d-k[i])/(double)s[i], ti[n-1]);
    }
    double ans = (double)(d)/ ti[0];
    printf("Case #%d: %lf\n", tc, ans);
  }
}
