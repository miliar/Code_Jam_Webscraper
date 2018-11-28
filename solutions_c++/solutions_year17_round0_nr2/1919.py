#include <cstdio>
#include <cstring>

char s[20];
int n;
char ans[20];

bool ok(int b, char c) {
  for (int i = b; i < n; ++i) {
    if (s[i] > c) return true;
    if (s[i] < c) return false;
  }
  return true;
}

void set(int b, char c) {
  for (int i = b; i < n; ++i) ans[i] = c;
}

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/B-large.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/bl.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    scanf("%s", s);
    memset(ans, 0, sizeof(ans));
    n = (int)strlen(s);
    char pre = '1';
    for (int i = 0; i < n; ++i) {
      char j;
      for (j = pre; j <= '9'; ++j) {
        if (!ok(i, j)) break;
      }
      pre = --j;
      if (pre < s[i]) {
        ans[i] = pre;
        set(i + 1, '9');
        break;
      } else {
        set(i, pre);
      }
    }
    printf("Case #%d: ", ++tc);
    if (ans[0] > '0') printf("%s", ans);
    else printf("%s", ans + 1);
    printf("\n");
  }
  return 0;
}