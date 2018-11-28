#include <iostream>
#include <algorithm>
using namespace std;
int p[51];
int prec = 1000000;
int main() {
  int t, n, k, in, de, u, ans;
  double a, b;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cin >> n >> k;
    ans = 10000;
    cin >> a;
    u = a*prec;
    for(int i = 0; i < n; i++) {
      cin >> a;
      p[i] = prec*a;
    }
    sort(p, p+n);
    while(u) {
      p[0]++;
      u--;
      for(int i = 1; i < n; i++) {
        if(p[i] < p[i-1]) {
          in = p[i];
          p[i] = p[i-1];
          p[i-1] = in;
        }
        else {
          break;
        }
      }
    }
    double rans = 1;
    for(int i = n-1; i >= 0; i--) {
        rans *= ((double)p[i])/(double)prec;
    }
    printf("Case #%d: %.10lf\n", tc, rans);
  }
}
