#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solve(){
  char s[1005];
  int k;
  scanf("%s%d", s, &k);
  int len = strlen(s);
  for (int i = 0; s[i] ; ++i){
    s[i] = s[i] == '-' ? 0 : 1;
  }
  int i = 0 ,cnt = 0;
  for (; i + k - 1 < len; ++i){
    if ( !s[i] ){
      for (int j = i; j < i + k ; ++j) s[j] ^= 1;
      cnt++;
    }
  }
  for (; i < len; ++i)
    if ( !s[i] )
      return -1;
  return cnt;
}
int main(){
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i){
    int rc = solve();
    if ( rc == -1){
      printf("Case #%d: IMPOSSIBLE\n", i + 1);
    }else{
      printf("Case #%d: %d\n", i + 1, rc);
    }
  }
  return 0;
}
