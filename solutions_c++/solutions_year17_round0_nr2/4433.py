#include <bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
//#define tr(it,v) for(auto it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define ALL(G) (G).begin(),(G).end()

#if 1
#define DEB printf
#else
#define DEB(...)
#endif

typedef long long ll;
typedef long long LL;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int inft = 1000000009;
const int mod = 1000000007;
const int MAXN = 1000006;

/* Rozklad [1,M] na przedzialy bazowe np
   2302-> *,**,***,1***,20**,21**,22**,...
   go(0,1),go(0,2),...go(20,2),go(21,2),...
 */

ll best;
void go(ll pref,int stars){
//	printf("base %lld %d\n",pref,stars);
	vi V;
	while(pref){
		V.push_back(pref%10);
		pref/=10;
	}
	reverse(ALL(V));
	fru(i,stars)V.push_back(9);
	fru(i,V.size()-1)if(V[i]>V[i+1])return;
	ll ret=0;
	for(int a:V){
		ret*=10;ret+=a;
	}
	best=max(best,ret);
}
void rozklad(ll m){
//	printf("mam %lld\n",m);
	unsigned long long p=10;
	int k=1;
	while(p<=m+1){go(0,k);p*=10;k++;}
	p/=10;k--;
	ll d=1;
	while(p){
		if((d+1)*p<=m+1){go(d,k);d++;}
		else {p/=10;k--;d*=10;}
	}
}

void solve() {
	ll n;
	scanf("%lld",&n);
	best=1;
	rozklad(n);
	printf("%lld\n",best);
}

int main() {
	int te = 1;
	scanf("%d",&te);
	fru(ti,te) {
		printf("Case #%d: ",ti+1);
		solve();
	}
	return 0;
}
