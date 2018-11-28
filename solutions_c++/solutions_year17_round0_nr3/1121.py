#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define zero(x) (((x)>0?(x):-(x))<eps)
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int>PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int inf=0x3f3f3f3f;
const int INF=2e9+7;
const int mod=1e9+7;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
LL a[1000010];
map<LL,LL>p;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1;
    LL n,m,k;
    cin>>t;
    while(t--){
        cin>>n>>k;
        int cnt=0;
        printf("Case #%d: ",cas++);
        p.clear();
        a[cnt++]=n;
        p[n]=1;
        LL l,r,j=0;
        while(1){
            LL m=a[j++];
//            cout<<m<<" "<<p[m]<<endl;
            if(m&1LL) l=r=m>>1;
            else r=m>>1,l=(m>>1)-1;
            k-=p[m];
            if(k<=0LL) break;
            if(!p[r]) a[cnt++]=r;
            p[r]+=p[m];
            if(!p[l]) a[cnt++]=l;
            p[l]+=p[m];
        }
        cout<<r<<" "<<l<<endl;
    }
    return 0;
}
