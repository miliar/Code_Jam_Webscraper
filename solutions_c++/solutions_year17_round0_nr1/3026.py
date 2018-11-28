#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char s[1505];
int n;

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1;t <= T;++t) {
    printf("Case #%d: ", t);
    scanf("%s %d", s, &n);

    int len = strlen(s);
    int ans = 0;
    for(int i = len-1;i >= n-1;--i)
    if(s[i] != '+') {
      ++ans;
      for(int k = i-n+1;k <= i;++k)
        if( s[k] == '+' ) s[k] = '-';
        else s[k] = '+';
    }

    for(int i = 0;i < n;++i) if( s[i] != '+' ) ans = -1;
    if(ans >= 0) printf("%d\n", ans);
    else printf("IMPOSSIBLE\n");
  }
}
