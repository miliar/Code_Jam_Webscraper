#include <bits/stdc++.h>
using namespace std;
int n,c,m;
int num[1009];
int s[1009];
int main(){
//    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d%d",&n,&c,&m);
        memset(num,0,sizeof num);
        memset(s,0,sizeof s);
        for(int i=0;i<m;++i){
            int p,b;
            scanf("%d%d",&p,&b);
            ++num[p];
            ++s[b];
        }
        int ans=0;
        for(int i=1;i<=c;++i)ans=max(ans,s[i]);
        for(int i=1,ss=0;i<=n;++i){
            ss+=num[i];
            ans=max(ans,(ss+i-1)/i);
        }
        int ans2=0;
        for(int i=1;i<=n;++i){
            if(num[i]>ans)ans2+=num[i]-ans;
        }
        printf("Case #%d: ",ca);
        printf("%d %d\n",ans,ans2);
    }
    return 0;
}
