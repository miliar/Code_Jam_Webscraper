#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define zero(x) (((x)>0?(x):-(x))<eps)
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int>PII;
typedef pair<double,int>PDI;
typedef pair<int,string>PIS;
const double eps=1e-8;
const double PI=acos(-1.0);
const LL INF=1e18;
const int mod=1e9+7;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int v[1005],per[1010];
VI g[1010];
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1,n,p,c,m,b,x,y;
    cin>>t;
    while(t--){
        cin>>n>>c>>m;
        int mx=0;
        memset(v,0,sizeof v);
        memset(per,0,sizeof per);
        for(int i=0;i<m;i++){
            cin>>x>>y;
            per[y]++;
            v[x]++;
            mx=max(per[y],mx);
        }
        int ans=0;
        for(int i=n;i>=1;i--){
            if(v[i]>mx){
                int g=v[i]-mx;
                ans+=g;
                v[i-1]+=g;
            }
        }
        if(v[0]) mx++,ans=0;
        printf("Case #%d: %d %d\n",cas++,mx,ans);
//        memset(v,0,sizeof v);
//        g[1].clear();
//        g[2].clear();
//        for(int i=0;i<m;i++){
//            cin>>p>>b;
//            g[b].pb(p);
//        }
//        int cnt=SZ(g[2]);
//        int ans=max(SZ(g[1]),cnt),res=0;
//        for(int i=1;i<=c;i++) sort(all(g[i]));
//        for(auto i:g[2]) v[i]++;
//        for(auto i:g[1]){
//            int f=1;
//            for(auto j:g[2]){
//                if(v[j]&&i!=j){
//                    v[j]--;
//                    cnt--;
//                    f=0;
//                    break;
//                }
//            }
//            if(!cnt) break;
//            if(f){
//                if(i==1){
//                    ans++;
//                }
//                else {
//                    v[i]--;
//                    cnt--;
//                    res++;
//                }
//
//            }
//        }
    }
    return 0;
}
/*
*/

