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
typedef double ld;
typedef pair< ll,ll > pi;
typedef pair< ll,pi > pii;
typedef vector< ll > vi;
typedef vector< pi > vii;
const ll mod=51123987;
const ll inf=121;
ll powmod(ll a,ll b){ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
template<typename N>N gcd(N a,N b){return b?gcd(b,a%b):a;}
void precision(ll pr){ cout.precision(pr); cout<<fixed; }

const int N=1e6+21;
vi v,a;
ll x,y;
void f(ll n){
    while(n){
        v.pb(n%10);
        n/=10;
    }
    reverse(all(v));
}
void f2(){
    ll i;
    for(i=1;i<sz(v);i++){
        if(v[i]<v[i-1]){
            if(v[i]==0&&v[i-1]==1){
                y=1; break;
            }
            else{
                x=1; break;
            }
        }
    }
    if(y)
        rep(i,0,sz(v)-2) a.pb(9);
    else if(x){
        for(int j=0;j<i-1;j++) a.pb(v[j]);
        a.pb(v[i-1]-1);
        for(int j=i;j<sz(v);j++) a.pb(9);
    }
    else rep(i,0,sz(v)-1) a.pb(v[i]);
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    ll i,j,T,k,n,t;
    cin>>T;
    for(t=1;t<=T;t++){
        cout<<"Case #"<<t<<": ";
        cin>>n;
        v.clear(); a.clear(); x=y=0;
        f(n);
        rep(i,0,18){
            x=y=0; a.clear();
            f2();
            v.clear();
            rep(j,0,sz(a)-1) v.pb(a[j]);
        }
        rep(i,0,sz(a)-1) cout<<a[i];
        cout<<'\n';
    }
    return 0;
}
