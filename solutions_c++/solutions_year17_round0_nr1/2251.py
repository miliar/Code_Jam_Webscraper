#include <bits/stdc++.h>
using namespace std;

char str[1111];

int main(void) {

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);
    scanf(" %s", str);
    int n = strlen(str);
    int K = 0; scanf("%d", &K);
    bool ok = true;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (str[i] == '-') {
        ++ans;
        if (i+K <= n) {
          for (int j = i; j < i+K; ++j) {
            if (str[j] == '-') {
              str[j] = '+';
            } else {
              str[j] = '-';
            }
          }
        } else {
          ok = false;
          break;
        }
      }
      // printf("%s\n", str);
    }
    if (ok) {
      printf("%d\n", ans);
    } else {
      puts("IMPOSSIBLE");
    }
  }

  return 0;
}