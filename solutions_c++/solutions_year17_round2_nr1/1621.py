#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long
using namespace std;
int test,n;
double st[1007],tim[1007],pos[1007],sp[1007],goal,pl=0;
long long k,a,b;
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&test);
    for(int t=1;t<=test;t++){
        pl=0;
        printf("Case #%d: ",t);
        scanf("%lld %d",&k,&n);
        for(int i=1;i<=n;i++){
            scanf("%lld %lld",&a,&b);
            pos[i]=(double) a;
            sp[i]=(double) b;
        }
        goal=(double) k;
        for(int i=n;i>=1;i--){
            tim[i]=(goal-pos[i])/sp[i];
            pl=max(pl,tim[i]);
            //printf("%.7lf\n",tim[i]);
        }
        double ans=goal/pl;
        printf("%.7lf\n",ans);
    }
}
