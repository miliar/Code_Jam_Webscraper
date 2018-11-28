#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[100005];
int k;

int main(void) {
  int t;
  while(scanf("%d", &t) != -1) {
    for(int tt = 1; tt <= t; tt += 1) {
      scanf("%s%d", s, &k);
      int len = strlen(s);
      int cnt = 0;
      for(int i = 0; i < len - k + 1; i += 1) {
        if(s[i] == '-') {
          for(int j = i + k - 1; j >= i; j -= 1) {
            s[j] = s[j] == '-' ? '+' : '-';
          }
          cnt += 1;
        }
      }
      int flag = 1;
      for(int i = 0; flag && i < len; i += 1) {
        if(s[i] == '-') {
          flag = false;
        }
      }
      if(flag) {
        printf("Case #%d: %d\n", tt, cnt);
      } else {
        printf("Case #%d: IMPOSSIBLE\n", tt);
      }
    }
  }
  return 0;
}
