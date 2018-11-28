//IIT Kanpur FacelessMen India
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

//#define DEBUG
ll power(ll x,ll y){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%mod;
    else y/=2,x=x*x%mod;
  }
  return t;
}
#ifdef DEBUG
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define dprintf(fmt,...)
#endif

string get(ll z){
  string s;
  while(z) s.pb(z%10+'0'),z/=10;
  reverse(all(s));
  return s;
}
int ys(int z){
  string a = get(z);
  string b=a;
  sort(all(b));
  if(a==b) return 1;
  return 0;
}
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(aa,t){
    ll n; scanf("%lld",&n);
    string g = get(n);
    ll ans=0;
    int z=0;
    while(z<g.size()-1){
      if(g[z+1]<g[z]){
        if(g[z]=='1'){
          REP(i,g.size()-1) ans=ans*10+9;
        }else{
          int fl=0;
          REP(i,g.size()) if(fl){
            ans=ans*10+9;
          }else{
            int ch = min(g[z]-1,(int)g[i]);
            ans=ans*10+ch-'0';
            if(ch<g[i]) fl=1;
          }
        }
        break;
      }else z++;
    }
    if(z==g.size()-1){
      ans=n;
    }
   //  int su=0;
   //  REPP(i,1,n+1) if(ys(i)) su=i;
   // // printf("%lld %d %lld\n",n,su,ans);
   //  assert(su==ans);
    printf("Case #%d: %lld\n",aa+1,ans);
  }
  return 0;
}
