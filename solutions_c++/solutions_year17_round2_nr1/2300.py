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
#define sz(s) (int)s.size()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

ll power(ll x,ll y){
	ll t=1;
	while(y>0){
		if(y%2) y-=1,t=t*x%mod;
		else y/=2,x=x*x%mod;
	}
return t;
}

int main(){
	int t;
	scanf("%d",&t);
	REP(kase,t){
		int n,d,a,b;
		scanf("%d%d",&d,&n);
		double x=INF,D=d,X,Y;
		REP(i,n){
			scanf("%d%d",&a,&b);
			X=a,Y=b;
			x=min(x,D*Y/(D-X));
		}
		printf("Case #%d: %.9lf\n",kase+1,x);
	}
	return 0;
}