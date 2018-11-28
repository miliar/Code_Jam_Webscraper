#include <stdio.h>
#include <string.h>

char s[2000];
int m;
int flip(int x) {
  for(int i = 0; i < m ; i++) {
    if (s[x+i] == '+') s[x+i] = '-';
    else if (s[x+i] =='-') s[x+i] = '+';
  }
}
int main() {
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e < t ; e++) {
    scanf("%s",s);
    scanf("%d",&m);
    int ans = 0;
    int n = strlen(s);
    for(int i = 0 ; i < n ; i++) {
      if (i <= n-m) {
        if (s[i] == '-') {
          flip(i);
          ans++;
        }
      } else {
        if (s[i] == '-') ans = -1;
      }
    }
    printf("Case #%d: ", e+1);
    if (ans == -1) printf("IMPOSSIBLE");
    else printf("%d",ans);
    printf("\n");
  }
}
