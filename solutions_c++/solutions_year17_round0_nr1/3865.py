#include <bits/stdc++.h>
#define REP(i,x,y) for(int i=x;i<(y);++i)
using namespace std;
int k;
char s[1010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;scanf("%d",&T);int cas=1;
    while(T--){
        scanf(" %s",s);
        scanf("%d",&k);
        int len=strlen(s),cnt=0;
        REP(i,0,len-k+1){
            if(s[i]=='-') {
                REP(j,i,i+k) {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
                cnt++;
            }
        }
        int flag=1;
        REP(i,0,len) if(s[i]=='-') flag=0;
        if(flag) printf("Case #%d: %d\n",cas++,cnt);
        else printf("Case #%d: IMPOSSIBLE\n",cas++);
    }
}
