#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAXN 2000
double f[MAXN][MAXN];

int main(void) {
  int T;
  scanf("%i", &T);
  
  for (int t = 1; t <= T; t++) {
    int n, k;
    scanf("%i %i", &n, &k);
    
    vector<pair<long long, long long>> a(n);
    for (int i = 0; i < n; i++) {
      scanf("%lld %lld", &a[i].first, &a[i].second);
    }
    sort(a.rbegin(), a.rend());
    
    const double oo = 1e15;
    for (int i = 0; i <= n+10; i++) {
      for (int j = 0; j <= n+10; j++) {
        f[i][j] = -oo;
      }
    }
    
    f[n][k] = 0;
    for (int i = n-1; i >= 0; i--) {
      for (int j = 0; j <= n; j++) {
        double area = 2 * M_PI * a[i].first * a[i].second;
        f[i][j] = max(f[i+1][j], f[i+1][j+1] + area);
      }
    }
    
    double ans = -oo;
    for (int i = 0; i < n; i++) {
      double area = 2 * M_PI * a[i].first * a[i].second;
              area += M_PI * a[i].first * a[i].first;
      ans = max(ans, area + f[i+1][1]);
    }
    
    printf("Case #%i: %.8f\n", t, ans);
  }
  
  return 0;
}