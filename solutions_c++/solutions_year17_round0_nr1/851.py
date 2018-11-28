#include <stdio.h>
#include <cstring>
#include <string>

const int N=1010;
char s[N];

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int test,k,cas(1);
  scanf("%d",&test);
  while(test--){
    scanf("%s%d",s,&k);
    int n=strlen(s);
    int ans(0);
    for(int i = 0;i < n; ++i){
      if(s[i] == '-'){
        ++ans;
        if(i+k>n) {
          ans=-1;
          break;
        }
        for(int j = 0; j < k; ++j){
          if(s[i+j] == '-') s[i+j] = '+';
          else s[i+j] = '-';
        }
      }
    }
    if(ans == -1){
      printf("Case #%d: IMPOSSIBLE\n",cas++);
    }else{
      printf("Case #%d: %d\n",cas++,ans);
    }
  }
  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
