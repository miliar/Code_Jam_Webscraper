#include <stdio.h>
#include <string.h>

char ans[20];

bool f(char* s, int pos) {
  if (*s == '\0') {
    ans[pos] = '\0';
    return true;
  }
  if (pos > 0 && s[0] < ans[pos - 1]) return false;
  ans[pos] = s[0];
  if (f(s + 1, pos + 1)) return true;
  // not success
  if (pos > 0 && s[0] - 1 < ans[pos - 1]) return false;
  ans[pos] = s[0] - 1;
  int n = strlen(s);
  for (int i = 1; i < n; ++i)
    ans[pos + i] = '9';
  ans[pos + n] = '\0';
  return true;
}

int main() {
  int T;
  char s[20], *p;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%s", s);
    f(s, 0);
    p = ans;
    while (*p == '0') ++p;
    printf("Case #%d: %s\n", t, p);
  }
  return 0;
}
