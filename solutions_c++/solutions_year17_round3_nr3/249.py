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
const double eps=1e-8;
const double pi=acos(-1.0);
const int INF=0x3f3f3f3f;
const int mod=1e9+7;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
double p[55];
int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1,n,k;
    double u;
    cin>>t;
    while(t--){
        cin>>n>>k>>u;
        for(int i=0;i<n;i++){
            cin>>p[i];
        }
        sort(p,p+n);
        p[n]=1.0;
        while(fabs(u)>eps){
            for(int i=1;i<=n;i++){
                if(p[i]!=p[i-1]){
                    double c=p[i]-p[i-1];
                    double d=min(c*i,u);
                    u-=d;
                    for(int j=0;j<i;j++){
                        p[j]+=d/i;
                    }
                    break;
                }
            }
//            cout<<u<<endl;
        }
        double ans=1;
        for(int i=0;i<n;i++) ans*=p[i];
        printf("Case #%d: %.10f\n",cas++,ans);
    }
    return 0;
}

