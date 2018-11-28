#include <bits/stdc++.h>
#define maxn 1010
#define REP(i,x,y) for(int i=x;i<(y);i++)
using namespace std;
struct P{
    double r,h,area1,area2;
    int id;
}pp[maxn],tmp[maxn];
int n,k;
const double pi=acos(-1.0);
inline bool cmp(const P& a,const P& b){
    return a.r>b.r;
}
inline bool cmp2(const P& a,const P& b){
    return a.area2>b.area2;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        memset(pp,0,sizeof(pp));
        scanf("%d %d",&n,&k);
        REP(i,1,n+1) {
            scanf("%lf %lf",&pp[i].r,&pp[i].h);
            pp[i].area1=pi*pp[i].r*pp[i].r;pp[i].area2=pp[i].h*2*pi*pp[i].r;
            pp[i].id=i;
        }
        double ans=0.0;
        sort(pp+1,pp+1+n,cmp);
        //REP(i,1,n+1) cout<<pp[i].r<<" "<<pp[i].h<<" "<<pp[i].area2<<endl;
        REP(i,1,n-k+2){
            memset(tmp,0,sizeof(tmp));
            int cnt=0;
            double res=pp[i].area1+pp[i].area2;
            REP(j,i+1,n+1) tmp[++cnt]=pp[j];
            sort(tmp+1,tmp+1+cnt,cmp2);
            REP(j,1,k) res+=tmp[j].area2;
            ans=max(ans,res);
        }
        printf("Case #%d: %.20f\n",cas++,ans);
    }
}
