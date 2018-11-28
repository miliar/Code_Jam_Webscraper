#include <bits/stdc++.h>

const int maxn = 1010;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tests;
  scanf("%d", &tests);
  char s[maxn];
  int k;
  int test_number = 0;
  while (tests--) {
    scanf("%s %d", s, &k);
    int len = strlen(s);
    bool ok = true;
    int cnt = 0;
    for (int i = 0; i <= len - k; i++) {
      if (s[i] == '+') {
        continue;
      }
      cnt++;
      for (int j = i; j < i + k; j++) {
        s[j] = (s[j] == '+') ? '-' : '+';
      }
    }
    for (int i = len - k + 1; i < len; i++) {
      if (s[i] == '-') {
        ok = false;
      }
    }
    printf("Case #%d: ", ++test_number);
    if (!ok) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", cnt);
    }
  }
  return 0;
}
