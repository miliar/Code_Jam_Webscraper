//AGHORii
#include<bits/stdc++.h>
#define rep(a,b,c) for((a)=(int)(b);(a)<=(int)(c);(a)++)
#define per(a,b,c) for((a)=(int)(c);(a)>=(int)(b);(a)--)
#define mem(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,(-1),sizeof(a))
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define pb push_back
#define MP make_pair
#define fi first
#define se second
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define sz(x) ((int)((x).size()))
#define all(x) ((x).begin()), ((x).end())
#define rall(x) ((x).rbegin()), ((x).rend())

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair< ll,ll > pi;
typedef pair< ll,pi > pii;
typedef vector< ll > vi;
typedef vector< pi > vii;
const ll mod=51123987;
const ll inf=1e12+21;
ll powmod(ll a,ll b){ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
template<typename N>N gcd(N a,N b){return b?gcd(b,a%b):a;}
void precision(ll pr){ cout.precision(pr); cout<<fixed; }

const int N=1e6+21;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2-out.txt","w",stdout);
    ll i,j,k,t,T;
    cin>>T;
    for(t=1;t<=T;t++){
        ll ans=0;
        cout<<"Case #"<<t<<": ";
        string s="";
        cin>>s;
        cin>>k;
        for(i=0;i+k-1<s.length();++i){
            if(s[i]=='-'){
                for(j=i;j<=i+k-1;++j){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            ++ans;
            }
        }
        ll sw=0;
        rep(i,0,sz(s)) if(s[i]=='-') sw=1;
        if(sw) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<'\n';
    }
    return 0;
}
