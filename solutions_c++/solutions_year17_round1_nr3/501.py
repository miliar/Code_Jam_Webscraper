#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
int T_T;
int oHd;
int Hd,Ad,Hk,Ak,B,D;
int ans;

void dfs(int Hd,int Ad,int Hk,int Ak,int step)
{
    //printf("step = %d\n",step);
    if (Hd <= 0) return ;
    if (step >= ans) return ;
    if (Hk <= Ad) {ans = min(ans,step); return ;}
    if (Hd-Ak <= 0) dfs(oHd-Ak,Ad,Hk,Ak,step+1);
    if (B) dfs(Hd-Ak,Ad+B,Hk,Ak,step+1);
    dfs(Hd-Ak,Ad,Hk-Ad,Ak,step+1);
    if (Ak > 0 && D) dfs(Hd-max(0,Ak-D),Ad,Hk,Ak-D,step+1);
}
int main(void)
{
    #ifdef LOCAL
    freopen("C-small-attempt0.in","r",stdin);
    //freopen("out-small.txt","w",stdout);
    #endif // LOCAL
    scanf("%d",&T_T);
    for (int cas=1;cas<=T_T;cas++)
    {
        scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
        oHd = Hd;
        ans = 444;
        dfs(Hd,Ad,Hk,Ak,1);
        printf("Case #%d: ",cas);
        if (ans >= 404) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
