#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
const int N = 1e3+5;
char s[N];
int T,n,k,kase;
int main(){
    freopen("E:\\workspace\\A-large.in","r",stdin);
    freopen("E:\\out.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
      scanf("%s%d",s+1,&k);
      n=strlen(s+1);
      int ret = 0;
      for(int i=1;i<=n;++i){
         if(s[i]=='+')continue;
         if(i+k-1>n){
              ret = -1;
              break;
         }
         ++ret;
         for(int j=i;j<=i+k-1;++j){
            if(s[j]=='+')s[j]='-';
            else s[j]='+';
         }
      }
      printf("Case #%d: ",++kase);
      if(ret==-1)printf("IMPOSSIBLE\n");
      else printf("%d\n",ret);
    }
    return 0;
}