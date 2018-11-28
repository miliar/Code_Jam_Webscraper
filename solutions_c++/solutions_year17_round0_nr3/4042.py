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

set<ll> S;
priority_queue<pair<pll,int> > P;
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(aa,t){
    ll n,k; scanf("%lld%lld",&n,&k);
    S.clear(); 
   // printf("do\n");
    while(!P.empty()) P.pop();//,printf("%d\n",(int)P.size());
    S.insert(0); S.insert(n+1);
    ll m = (n+1)/2;
    //printf("gg\n");
    P.push(mp(mp((m-1),n-m),-m));

    pair<pll,int> cur;
    while(k){
      k--;
     /// printf("zz\n");
      //assert(P.size()>0);
      cur = P.top(); P.pop();
      cur.Y*=-1;
      set<ll> :: iterator it=S.lower_bound(cur.Y);
      set<ll> :: iterator it2=it;
      it--;
      int prv = *(it),ft = *(it2);
      S.insert(cur.Y);
      //printf("%d %d %d\n",cur.Y,prv,ft);
      if(prv+1<cur.Y){
        ll m = (prv+cur.Y)/2;

        P.push(mp(mp(m-prv-1,cur.Y-m-1),-m));
      }
      if(cur.Y+1<ft){
        ll m = (cur.Y+ft)/2;
        P.push(mp(mp(m-cur.Y-1,ft-m-1),-m));
      }
    }
    printf("Case #%d: %lld %lld\n",aa+1,cur.X.Y,cur.X.X);
  }
  return 0;
}
