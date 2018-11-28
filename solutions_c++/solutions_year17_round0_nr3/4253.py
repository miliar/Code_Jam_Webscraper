#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(void) {
  int T; scanf("%d", &T);

  for (int ijk = 0; ijk < T; ijk++) {
    int n, k; scanf("%d%d", &n, &k);

    vector<int> a;
    a.push_back(0);
    a.push_back((n+1)/2);
    a.push_back(n+1);
    for (int i = 0; i < k-1; i++) {
      int l = 0, p = 0;
      for (int j = 0; j+1 < int(a.size()); j++) {
        if (l < a[j+1]-a[j]) {
          p = j;
          l = a[j+1]-a[j];
        }
      }
      a.push_back((a[p]+a[p+1])/2);
      sort(a.begin(), a.end());
    }

    int mlr, alr; mlr = n+1; alr = 0;
    for (int i = 1; i+1 < int(a.size()); i++) {
      int v = min(a[i]-a[i-1]-1, a[i+1]-a[i]-1);
      int w = max(a[i]-a[i-1]-1, a[i+1]-a[i]-1);
      if (mlr > v) {
        mlr = v;
        alr = w;
      }
      if (mlr == v) {
        alr = min(alr, w);
      }
    }
    printf("Case #%d: %d %d\n", ijk+1, alr, mlr);
  }
  return 0;
}
