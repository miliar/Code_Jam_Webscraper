#include <cstring>
#include <cstdio>

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int R, C;
    int pending = 0;
    char cur[100] = {0}, last[100] = {0};
    scanf("%d%d", &R, &C);
    printf("Case #%d:\n", t + 1);
    for (int i = 0; i < R; ++i) {
      scanf("%99s", cur);
      for (int j = 0; j < C; ++j) {
        if (cur[j] != '?') {
          for (int k = j; k > 0; --k) {
            cur[k - 1] = cur[k];
          }
          ++j;
          while (j < C) {
            if (cur[j] == '?') {
              cur[j] = cur[j - 1];
            }
            ++j;
          }
          goto good;
        }
      }
      if (pending >= 0) {
        ++pending;
      } else {
        printf("%s\n", last);
      }
      continue;
good:
      if (pending >= 0) {
        while (pending) {
          printf("%s\n", cur);
          --pending;
        }
        pending = -1;
      }
      printf("%s\n", cur);
      strcpy(last, cur);
    }
  }
  return 0;
}
