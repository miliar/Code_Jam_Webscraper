#include <stdio.h>
#include <cstring>
#include <algorithm>

using namespace std;

int cnt[4];
int main()
{
  freopen("A-small-attempt1.in","r",stdin);
  freopen("A-small-attempt1.out","w",stdout);
  int n,p;
  int test,cas(1);
  scanf("%d",&test);
  while(test--){
    scanf("%d%d",&n,&p);
    cnt[0]=cnt[1]=cnt[2]=cnt[3]=0;
    for(int j,i = 0; i < n; ++i){
      scanf("%d",&j); 
      cnt[j%p]++;
    }
    int ans(cnt[0]);
    if(p==2) {
      ans += cnt[1] / 2 + cnt[1]%2;
    }else if(p==3){
      int v = min(cnt[1],cnt[2]);
      ans += v;
      cnt[1] -= v; cnt[2] -= v;
      if(cnt[1]) {
        ans += cnt[1] / 3 + ((cnt[1]%3)>0);
      }
      if(cnt[2]) {
        ans += cnt[2] / 3 + ((cnt[2]%3)>0);
      }
    }else{
      {
        int v = min(cnt[1],cnt[3]);
        ans += v; 
        cnt[1] -= v; cnt[3] -= v;
      }
      {
        ans += cnt[2]/2;
        cnt[2] %= 2;
      }
      {
        if(cnt[2]){
          if(cnt[1] >= 2 || cnt[3] >= 2){
            ans++;
            int v= max(cnt[1],cnt[3])-2;
            ans += v/4 + (v%4 > 0);
          }else{
            ans++;
          }
        }else {
            int v= max(cnt[1],cnt[3])-2;
            if(v){
              ans += v/4 + (v%4 > 0);
            }
        }
      }
    }
    printf("Case #%d: %d\n",cas++,ans);
  }



  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
