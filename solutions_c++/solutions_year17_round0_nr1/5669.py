#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N,K,len;
char str[1005];

int main(){
  freopen("A-large.in","r",stdin);
  scanf("%d",&N);
  for(int tt=1;tt<=N;tt++){
    scanf("%s %d",&str[1],&K);
    len = strlen(&str[1]);

    int ans = 0;
    for(int i=1;i<=len-K+1;i++){
      if(str[i] != '+'){
        ans++;
        for(int j=i;j<=i+K-1;j++){
          if(str[j] == '+')str[j] = '-';
          else str[j] = '+';
        }
      }
    }

    bool pass = true;
    for(int j=1;j<=len;j++) if(str[j] != '+') pass = false;

    if(pass) printf("Case #%d: %d\n",tt, ans);
    else printf("Case #%d: IMPOSSIBLE\n",tt);
  }
  return 0;
}
