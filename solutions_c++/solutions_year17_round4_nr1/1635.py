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
int v[5];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1,n,p,x;
    cin>>t;
    while(t--){
        cin>>n>>p;
        memset(v,0,sizeof v);
        for(int i=0;i<n;i++){
            cin>>x;
            v[x%p]++;
        }
        int ans=v[0];
        if(p==2) ans+=(v[1]+1)/2;
        else if(p==3){
            int g=min(v[1],v[2]);
            ans+=g;
            v[1]-=g;
            v[2]-=g;
            g=v[1]+v[2];
            ans+=(g+2)/3;
        }
        else {
            ans+=v[2]/2;
            int g=min(v[1],v[3]);
            ans+=g;
            v[1]-=g;
            v[3]-=g;
            g=v[1]+v[2];
            if(v[2]&&g>=2){
                ans++;
                g-=2;
            }
            ans+=(g+3)/4;
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
/*
*/

