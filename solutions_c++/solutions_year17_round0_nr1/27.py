#include <cstdio>
#include <cstring>
const int maxn = 1000 + 1;

int n, m;
char s[maxn];

int main(void) {
  int t, num = 0;
  scanf("%d", &t);
  while (t--) {
    scanf("%s", s);
    n = strlen(s);
    scanf("%d", &m);
    int ans = 0;
    for (int i = 0; i + m <= n; ++i) {
      if (s[i] == '-') {
        ++ans;
        for (int j = 0; j < m; ++j) {
          if (s[i + j] == '-') {
            s[i + j] = '+';
          } else {
            s[i + j] = '-';
          }
        }
      }
    }
    bool finish = true;
    for (int i = 0; i < n; ++i) {
      if (s[i] == '-') {
        finish = false;
        break;
      }
    }
    if (!finish) {
      printf("Case #%d: IMPOSSIBLE\n", ++num);
    } else {
      printf("Case #%d: %d\n", ++num, ans);
    }
  }
  return 0;
}
