#include <cstdio>
#include <algorithm>

using namespace std;

int main(void) {
  int T, d, n;
  int test_case = 1;
  scanf("%d", &T);
  while (T--) {
    double last_horse_time = 0.0;

    scanf("%d %d", &d, &n);
    for (int i = 0; i < n; ++i) {
      int k, s;
      scanf("%d %d", &k, &s);

      last_horse_time = max(last_horse_time, (1.0 * d - k) / s);
    }
  
    printf("Case #%d: %.6lf\n", test_case++, d / last_horse_time);
  }
  return 0;
}
