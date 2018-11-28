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

int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(aa,t){
    string s;
    int k;
    cin>>s>>k;
    int ans=0;
    REP(i,max(0,(int)s.size()-k+1)) if(s[i]=='-'){
      ans++;
      REPP(j,i,i+k){
        s[j]=(int)'+'+'-'-s[j];
       // printf("%d %c\n",j,s[j]);
      }
    }
    int fl=1;
    REP(i,s.size()) if(s[i]=='-') fl=0;
    printf("Case #%d: ",aa+1);
    if(fl==0){
      printf("IMPOSSIBLE\n");
    }else printf("%d\n",ans);
  }
  return 0;
}
