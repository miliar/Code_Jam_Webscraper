#include <stdio.h>
#include <string.h>

int T, k, P[1010];
char A[1010];

int getState(char ch) {
  return ch == '-' ? 1 : 0;
}

int solve() {
  memset(P, 0, sizeof(P));
  int ret = 0, cur = 0, n = strlen(A);
  for (int i = 0 ; i < n ; ++i) {
    cur += P[i];
    int state = getState(A[i]);
    if (state ^ (cur & 1)) {
      if (i + k > n) {
        return -1;
      }
      ++ret;
      ++cur;
      --P[i + k];
    }
  }
  return ret;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; ++t) {
    scanf("%s%d", A, &k);
    int ans = solve();
    printf("Case #%d: ", t);
    if (ans == -1) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", ans);
    }
  }
}