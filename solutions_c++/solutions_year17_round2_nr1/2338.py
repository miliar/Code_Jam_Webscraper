#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair<int, int> Node;
const int maxn = 1000;
Node v[maxn+5];
int d, n;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%d%d", &d, &n);
    for(int i = 0; i < n; i++) {
      scanf("%d%d", &v[i].first, &v[i].second);
    }
    sort(v, v+n);
    double time = (double) (d - v[n-1].first) / v[n-1].second;
    for(int i = n - 2; i >= 0; i--) {
      double ti = (double) (d - v[i].first) / v[i].second;
      time = max(time, ti);
    }
    printf("Case #%d: %.8lf\n", kase, d / time);
  }
  return 0;
}
