#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

const int maxn = 1000;
const double pi = acos(-1);
typedef long long ll;
pair<int, int> a[maxn];
ll v[maxn];

int main(void) {
  int T, n, k;
  scanf("%d", &T);
  for (int case_id = 1; case_id <= T; ++case_id) {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) {
      int r, h;
      scanf("%d%d", &r, &h);
      a[i] = make_pair(r, h);
    }
    sort(a, a + n);
    long long ans = 0;
    for (int i = k - 1; i < n; ++i) {
      long long sum = (ll)a[i].first * a[i].first;
      for (int j = 0; j <= i; ++j) {
        v[j] = 2LL * a[j].first * a[j].second;
      }
      sort(v, v + i);
      for (int j = 0; j < k; ++j) {
        sum += v[i - j];
      }
      ans = max(ans, sum);
    }
    printf("Case #%d: %.10f\n", case_id, ans * pi);
  }
  return 0;
}
