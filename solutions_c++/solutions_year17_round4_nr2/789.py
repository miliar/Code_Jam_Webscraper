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
int deg[N];

int emp[N];
int ext,n;
int calc(int zo){
  ext=0;
  int cur=0;
  for(int i=n-1;i>=0;i--){
    ///emp[ak[i]]++;
    if(emp[i]>zo){
      ext+=emp[i]-zo; cur+=emp[i]-zo;
    }else{
      int fo = min(cur,zo-emp[i]);
      cur-=fo;
    }  
  }
  //printf("%d\n",cur);
  return cur==0;
}
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
 
  REP(aa,t){
    int c,m; scanf("%d%d%d",&n,&c,&m);
   // printf("%d %d %d\n",n,c,m);
    REP(i,c) deg[i]=0;
    REP(i,n) emp[i]=0;
    //ak.clear();
    REP(i,m){
      int a,b; scanf("%d%d",&a,&b); a--;b--;
      emp[a]++;
      deg[b]++;
    }
    //sort(all(ak));
  //  reverse(all(ak));
    int l=0,r=m;
    REP(i,n) l=max(l,deg[i]);
    while(l<r){
      int m=(l+r)/2;
      if(calc(m)) r=m; else l=m+1;
    }
    calc(l);
    printf("Case #%d: %d %d\n",aa+1,l,ext);
  }  
  return 0;
}
