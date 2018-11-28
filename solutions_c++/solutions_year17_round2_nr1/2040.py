#include <bits/stdc++.h>
#define maxn 100010
#define inf 0x3f3f3f3f
#define REP(i,x,y) for(int i=x;i<(y);i++)
#define RREP(i,x,y) for(int i=x;i>(y);i--)

using namespace std;
typedef long long ll;
typedef pair<int,int>pii;
int n,D;
struct P{
    int pos,v;
}pp[maxn];
const double eps=1e-12;
bool check(double vv){
    REP(i,1,n+1){
        if(pp[i].v>=vv) continue;
        double tmp1=1.0*D/vv;
        double tmp2=(1.0*D-1.0*pp[i].pos)/(double)pp[i].v;
        if(tmp1<=tmp2+eps) return false;
    }
    return true;
}
int main()
{
    freopen("data1.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        scanf("%d %d",&D,&n);
        REP(i,1,n+1)
            scanf("%d %d",&pp[i].pos,&pp[i].v);
        double L=0.0,R=1e20,ans=0.0;
        int cnt=150;
        while(cnt--){
            double mid=(L+R)/2.0;
            if(check(mid)){
                L=mid;ans=mid;
            }
            else R=mid;
        }
        printf("Case #%d: %.10f\n",cas++,ans);
    }
}
