#include <cassert>
#include <cstdio>
#include <cstring>

#include <algorithm>

using std::max;

int solve ( int p, int *a, int step ) {
  if (step == 3) {
    int res = a[0], bonus = 0;
    for (int i = 1; i < p; i++) {
      if (p == 4 && i == 2)
        res += a[i] / 2, bonus = bonus || !!(a[i] % 2);
      else
        res += a[i] / p, bonus = bonus || !!(a[i] % p);
    }
    return res + bonus;
  }
  int res = solve (p, a, step + 1);
  if (step == 0 && p >= 3) {
    for (int i = 1; i <= a[1] && i <= a[p - 1]; i++) {
      // fprintf (stderr, "take %d + %d times: %d\n", 1, p - 1, i);
      a[1] -= i, a[p - 1] -= i;
      res = max (res, solve (p, a, step + 1) + i);
      a[1] += i, a[p - 1] += i;
    }
  }
  if (step == 1 && p >= 4) {
    for (int i = 1; i <= a[2] && 2 * i <= a[1]; i++) {
      a[2] -= i, a[1] -= 2 * i;
      res = max (res, solve (p, a, step + 1) + i);
      a[2] += i, a[1] += 2 * i;
    }
  }
  if (step == 2 && p >= 4) {
    for (int i = 1; i <= a[2] && 2 * i <= a[3]; i++) {
      a[2] -= i, a[3] -= 2 * i;
      res = max (res, solve (p, a, step + 1) + i);
      a[2] += i, a[3] += 2 * i;
    }
  }
  return res;
}

int main () {
  int tn;
  assert (scanf ("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    int n, p;
    assert (scanf ("%d%d", &n, &p) == 2);
    int cnt[p];
    memset (cnt, 0, sizeof (cnt[0]) * p);
    for (int i = 0; i < n; i++) {
      int x;
      assert (scanf ("%d", &x) == 1);
      cnt[x % p]++;
    }
    /*
    fprintf (stderr, "p = %d\n", p);
    for (int i = 0; i < p; i++)
      fprintf (stderr, "p[i=%d] = %d\n", i, cnt[i]);
     */
    int ans = solve (p, cnt, 0);
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
