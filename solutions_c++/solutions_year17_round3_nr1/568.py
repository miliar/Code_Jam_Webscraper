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
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define all(a)  a.begin(), a.end()
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const double eps = 1e-8;
#define EQ(a,b) (fabs((a)-(b))<eps)
inline int max(int a,int b){return a<b?b:a;}
inline int min(int a,int b){return a>b?b:a;}
inline ll max(ll a,ll b){return a<b?b:a;}
inline ll min(ll a,ll b){return a>b?b:a;}
const int mod = 1e9+7;
const int N = 1e6+10;
const ll inf = 1e18;

ll power(ll a,ll n){
	if(n==0){
		return 1;
	}
	ll b = power(a,n/2);
	b = b*b%mod;
	if(n%2) b= b*a%mod;
	return b;
}

int add(int a,int b){ return (a+b)%mod;}
int mul(int a,int b){ return (ll)a*b%mod;}


long double dp[1001][1001],pi = acos(-1.0);
int vis[1001][1001];
vector <pll> v;
int n,k; 

long double f(int i,int j){
	if(i==n){
		return 0;
	}
	if(vis[i][j]) return dp[i][j];
	vis[i][j]=1; 
	long double ret = f(i+1,j);
	if(j<k){
		if(j==0) ret = max(ret,f(i+1,j+1) + 2*pi*v[i].X*v[i].Y + pi*v[i].X*v[i].X);
		else ret = max(ret,f(i+1,j+1)+ 2*pi*v[i].X*v[i].Y);
	}
	// printf("%d %d %Lf\n",i,j,ret);
	return dp[i][j]=ret;
}

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int t; scanf("%d",&t);
	REP(tt,t){
		scanf("%d %d",&n,&k);
		FILL(vis,0);
		v.clear();
		REP(i,n){
			int r,h; scanf("%d %d",&r,&h); v.pb(mp(r,h));
		}
		sort(all(v)); reverse(all(v));
		printf("Case #%d: %.9Lf\n",tt+1,f(0,0));
	}
	return 0;
}


