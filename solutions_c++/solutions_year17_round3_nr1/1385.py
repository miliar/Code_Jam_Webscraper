#include<bits/stdc++.h>
using namespace std;
#define test() int t;scanf("%d",&t);for(int tno=1;tno<=t;tno++)
#define mp make_pair
#define pb push_back
#define wl(n) while(n--)
#define fi first
#define se second
#define all(c) c.begin(),c.end()
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi; 
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
#define sz(a) int((a).size())
#define ini(a,v) memset(a,v,sizeof(a))
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scs(s) scanf("%s",s);
#define gcd __gcd
#define debug() printf("here\n") 
#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define MOD 1000000007
#define inf ((1<<29)-1)
#define linf ((1LL<<60)-1)
const double eps = 1e-9;
//-----------------------------------------------------------------------------------------------

const int MAX = 1009;

int a[MAX]={0};
int n,k;
vector< pll >v;
ll dp[MAX][MAX];
ll func(int cur,int k){
  if(cur==n){
    if(k==0)
      return 0;
    return -linf;
  }
  if(k<0)
    return -linf;
  if(k==0)
    return 0;
  ll &ans = dp[cur][k];
  if(ans!=-1)
    return ans;
  ans = 2*v[cur].se*v[cur].fi + func(cur+1,k-1);
  ans = max(ans,func(cur+1,k));
  return ans;
}
int main()
{
  int i,j;
  test(){
    ini(dp,-1);
    sc2(n,k);
    for(i=0;i<n;i++){
      ll x,y;
      cin>>x>>y;
      v.pb(mp(x,y));
    }
    sort(all(v));
    reverse(all(v));
    ll ans = 0 ;
    for(i=0;i<n;i++){
      ll x = func(i+1,k-1);
      ans = max(ans,2*v[i].fi*v[i].se + v[i].fi*v[i].fi + x);
    }
    v.clear();
    double ans1 = acos(-1)*ans;
    printf("Case #%d: ",tno);
    printf("%.12lf\n",ans1);
  }
  return 0;
}