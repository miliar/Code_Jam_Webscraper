#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[100005];
long long n;

int main(void) {
  int t;
  while(scanf("%d", &t) != -1) {
    for(int tt = 1; tt <= t; tt += 1) {
      scanf("%lld", &n);
      sprintf(s, "%lld", n);
      int len = strlen(s);
      int nine = len;
      for(int i = len - 1; i > 0; i -= 1) {
        if(s[i] < s[i - 1]) {
          s[i] = '9';
          nine = i;
          int k = i - 1;
          if(s[k] != '0') {
            s[k] -= 1;
          } else {
            while(s[k] == '0') {
              s[k + 1] = '9';
              k -= 1;
            }
            s[k] -= 1;
          }
        }
      }
      for(int i = nine; i < len; i += 1) {
        s[i] = '9';
      }
      printf("Case #%d: %s\n", tt, s[0] == '0' ? s + 1 : s);
    }
  }
  return 0;
}
