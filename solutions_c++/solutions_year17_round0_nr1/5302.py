#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#define Maxlen 1000
using namespace std;
int t, k, ans;
char s[Maxlen + 10];
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &t);
  for (int i = 1;i <= t;++ i) {
    ans = 0;
    getchar();
    scanf("%s", s);
    scanf("%d", &k);
    for (int j = 0;j + k - 1 < strlen(s);++ j) {
      if (s[j] == '-') {
        ++ ans;
        for (int l = 1;l <= k;++ l)
          s[j + l  - 1] = (s[j + l - 1] == '-') ? '+' : '-';
      }
    }
    bool temp = true;
    for (int j = 0;j < strlen(s);++ j)
      if (s[j] == '-') {
        temp = false;
        break;
      }
    printf("Case #%d: ", i);
    if (temp)
      printf("%d\n", ans);
    else
      printf("IMPOSSIBLE\n");
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
