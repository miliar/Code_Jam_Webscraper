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
const int N = 1e3+10;
const ll INF = 1e18;

ll power(ll x,ll y){
	ll t=1;
	while(y>0){
		if(y%2) y-=1,t=t*x%mod;
		else y/=2,x=x*x%mod;
	}
return t;
}

set <int> s;
set <pair <pii, int> > m;

int main(){
	int t;
	scanf("%d",&t);
	REP(kase,t){
		int n,k;
		scanf("%d%d",&n,&k);
		s.clear();
		m.clear();
		s.insert(0);
		s.insert(n+1);
		m.insert(mp(mp(n/2,n-n/2-1),n/2+1));
		REP(i,k-1){
			int x=(*m.rbegin()).Y,y,z;
			typeof(m.begin()) it=m.end();
			it--;
			m.erase(it);
			y=*(s.upper_bound(x));
			typeof(s.begin()) ii=(s.upper_bound(x));
			ii--;
			z=*ii;
			s.insert(x);
			// printf("%d %d %d\n",z,x,y);
			int n1=(y-x-1),b=x;
			// printf("%d\n",n1);
			if (n1) m.insert(mp(mp(n1/2,n1-n1/2-1),b+n1/2+1));
			n1=(x-z-1),b=z;
			// printf("%d\n",n1);
			if (n1) m.insert(mp(mp(n1/2,n1-n1/2-1),b+n1/2+1));
		}
		printf("Case #%d: %d %d\n",kase+1,(*m.rbegin()).X.X,(*m.rbegin()).X.Y);
	}
	return 0;
}