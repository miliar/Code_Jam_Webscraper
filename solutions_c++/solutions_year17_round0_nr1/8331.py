#include <cstdio>
#include <cstring>

char s[2000];
int k;

int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", ++cas);
    memset(s, 0, sizeof(s));
    scanf("%s%d", s, &k);
    int cnt = 0;
    for (int i = 0; s[i]; ++i) {
      if (s[i] == '-') {
        if (s[i + k - 1]) {
          ++cnt;
          for (int j = 0; j < k; ++j) {
            s[i + j]  = s[i + j] == '+' ? '-' : '+';
          }
        } else {
          cnt = -1;
        }
      }
    }
    if (cnt != -1) {
      printf("%d\n", cnt);
    } else {
      puts("IMPOSSIBLE");
    }
  }
  return 0;
}
