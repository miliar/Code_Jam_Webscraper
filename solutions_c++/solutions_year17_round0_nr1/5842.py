#include<stdio.h>
#include<string>
using namespace std;
const int N = 1005;
int n;
char s[N];
int add[N],sum[N];
int k;
int main(){
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  int T;scanf("%d",&T);
  int cas = 1;
  while(T--){
      scanf("%s %d",s+1,&k);
      int len = strlen(s+1);
      memset(add,0,sizeof add);
      memset(sum,0,sizeof sum);
      int tot = 0;
      for(int i=1;i+k-1<=len;i++){
            add[i] += add[i-1];
            if((add[i]&1)^(s[i]=='+')==0){
                add[i]++;
                add[min(len+1,i+k)]--;
                tot++;
            }
      }
      for(int i=len-k+2;i<=len;i++){
          add[i] += add[i-1];
          if((add[i]&1)^(s[i]=='+')==0) tot = -1;
      }
      if(tot>-1) printf("Case #%d: %d\n",cas++,tot);
      else printf("Case #%d: IMPOSSIBLE\n",cas++);
  }
  return 0;
}
