#include <stdio.h>
#include <string.h>

using namespace std;

char s[1001];

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);

  int t, len, minus, k, res;
  scanf("%d", &t);

  for(int c = 1; t--; c++) {
    res = minus = 0;

    scanf("%s%d", s, &k);
    len = strlen(s);

    for(int i = 0; i < len; i++)
      if(s[i] == '-')
        minus++;

    if(minus == 0) {
      printf("Case #%d: %d\n", c, 0);
      continue;
    }

    for(int i = 0; minus && i < 1000; i++) {
      for(int i = 0; i < len; i++) {
        if(s[i] == '-') {
          for(int j = i; i + k <= len && j < i + k && j < len; j++) {
            if(s[j] == '-') {
              minus--;
              s[j] = '+';
            } else {
              minus++;
              s[j] = '-';
            }
          }

          res++;
        }
      }
    }

    if(minus != 0) printf("Case #%d: IMPOSSIBLE\n", c);
    else printf("Case #%d: %d\n", c, res);
  }

  return 0;
}
