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

int rr[55];
vector<pii> ing[55];
priority_queue<int> P;
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(aa,t){
    int n,p; scanf("%d%d",&n,&p);
    REP(i,n) scanf("%d",&rr[i]),ing[i].clear();
    REP(i,n) REP(j,p){
      int x; scanf("%d",&x);
      double l = 10.*x/9+EPS,r=10.*x/11-EPS;
      int lo = r/rr[i];
      if(lo*rr[i]*11/10.<x) lo++;
      //printf("g%lf %lf\n",l,r);
      int ro = l/rr[i];
      if(lo>ro) continue;
      ing[i].pb(mp(ro,lo));
     // printf("%d %d\n",lo,ro);
    }
    REP(i,n) sort(all(ing[i]));
    int ans=0;
    while(ing[0].size()){
      pii z = ing[0].back(); ing[0].pop_back();
      int fl=1;
      REPP(i,1,n) {
        int x=0;
        REP(j,ing[i].size()) {if(!(ing[i][j].Y>z.X||ing[i][j].X<z.Y)) x++;}//printf("%d %d %d %d\n",ing[i][j].X,ing[i][j].Y,ing[i][j].X>z.Y,ing[i][j].Y>z.X);}
        if(x==0) fl=0;
      }
      if(fl==0) continue;
      REPP(i,1,n) {
        int x=0,mx=-mod;
        REP(j,ing[i].size()) if(!(ing[i][j].Y>z.X||ing[i][j].X<z.Y)) {
          if(ing[i][j].Y>mx) {
            mx=ing[i][j].Y;
            x=j;
          }
        }
        ing[i].erase(ing[i].begin()+x);
      }
      ans++;
    }
    printf("Case #%d: %d\n",aa+1,ans);
  }
  return 0;
}
