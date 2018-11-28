#include <bits/stdc++.h>
using namespace std;

char str[1010];

int main() {
  freopen("a1.in", "r", stdin);
  freopen("a1.out", "w", stdout);
  int kase;
  scanf("%d", &kase);
  for(int ka = 0; ka < kase; ka++) {
    int n;
    scanf("%s%d", str, &n);
    int len = strlen(str);
    int tot = 0;
    for(int i = 0; i + n <= len; i++) {
      if(str[i] == '-') {
        tot++;
        for(int j = 0; j < n; j++) {
          str[i + j] = (str[i + j] == '+' ? '-' : '+');
        }
      }
    }
    printf("Case #%d: ", ka + 1);
    for(int i = 0; i < len; i++) {
      if(str[i] == '-') {
        printf("IMPOSSIBLE\n");
        goto nxt;
      }
    }
    printf("%d\n", tot);
    nxt:;
  }
  return 0;
}
