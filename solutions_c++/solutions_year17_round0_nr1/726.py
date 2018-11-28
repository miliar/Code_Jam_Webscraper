#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1e3 + 10;

char s[N];
int k;
bool c[N];

inline void solve () {
  for (int i = 0;i < N;i ++) {
    c[i] = false;
  }

  scanf ("%s %d", s + 1, &k);
  s[0] = '+';

  int n;
  for (int i = 1;s[i] != 0;i ++) {
    n = i;
    if (s[i] != s[i - 1]) {
      c[i] = true;
    }
  }

  int ans = 0;
  for (int i = 1;i <= n - k + 1;i ++) {
    if (c[i]) {
      c[i] = false;
      c[i + k] ^= true;
      ans ++;
    }
  }
  for (int i = n - k + 2;i <= n;i ++) {
    if (c[i]) {
      ans = -1;
    }
  }
  if (ans == -1) {
    printf ("IMPOSSIBLE\n");
  } else {
    printf ("%d\n", ans);
  }
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: ", i);
    solve ();
  }
}
