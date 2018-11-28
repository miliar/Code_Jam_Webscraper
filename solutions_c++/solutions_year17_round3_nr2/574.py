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

int Ac[2][2000];
int dp[2000][2000][2][2];

int f(int mn,int fst,int last, int pr){
	if(mn==720*2){
		if(fst!=720) return mod;
		if(pr!=last) return mod;
		return 0;
	}
	int &ret = dp[mn][fst][last][pr];
	if(ret!=-1) return ret;
	ret = mod;
	if(fst>720) return ret;
	if(Ac[pr][mn]){
		ret = min(ret, f(mn+1,mn+1-fst,last,pr^1)+1);
	}else{
		ret = min(ret,f(mn+1,fst+1,last,pr));
		if(!Ac[pr^1][mn])  ret = min(ret, f(mn+1,mn+1-fst,last,pr^1)+1);
	}
	// printf("%d %d %d %d %d\n",mn,fst,last,pr,ret);
	return ret;
}

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int t; scanf("%d",&t);
	REP(tt,t){
		int ac,aj;
		FILL(Ac,0); 
		FILL(dp,-1);
		scanf("%d%d",&ac,&aj);
		REP(i,ac){
			int a,b; scanf("%d %d",&a,&b); REPP(j,a,b) Ac[0][j]=1;
		}
		REP(i,aj){
			int a,b; scanf("%d %d",&a,&b); REPP(j,a,b) Ac[1][j]=1;
		}
		printf("Case #%d: %d\n",tt+1,min(f(0,0,0,0),f(0,0,1,1)));
	}
	return 0;
}


