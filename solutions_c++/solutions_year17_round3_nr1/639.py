#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,l,r) for(int i=(l);i<=(r);i++)

//#define DEBUG
#ifdef DEBUG
#define print(...) fprintf(stderr, __VA_ARGS__)
#else
#define print(...) 
#endif
#define dbg(x) cout<<#x<<" = "<<x<<endl

template<typename T,typename S>inline bool upmin(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool upmax(T&a,const S&b){return a<b?a=b,1:0;}
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))  //<--
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))

using namespace std;
typedef long long LL;
const int maxn=1e5+1;


struct jg {
	LL r,h;
	bool operator<(const jg &b) const {
		return r!=b.r?r>b.r:h>b.h;
	}
};

int n,k;
jg wu[1001];
LL f[2][1001];
int main() {
	int T; scanf("%d",&T);
	FOR (tt,1,T) {
		scanf("%d%d",&n,&k);
		FOR (i,1,n) scanf("%lld%lld",&wu[i].r,&wu[i].h);
		sort(wu+1,wu+1+n);

		int p=0;
		FOR (j,0,k) f[p][j]=0;

		for (int i=1;i<=n;i++) {
			LL r=wu[i].r,h=wu[i].h;
			p=!p;
			//for (int j=0;j<=k;j++) f[p][j]=f[!p][j];

			f[p][1]=max(f[!p][1],r*r+2*r*h);
			for (int j=2;j<=k;j++) {
				f[p][j]=max(f[!p][j],f[!p][j-1]+2*r*h);
			}
			//cout<<i<<" "<<f[p][1]*M_PI<<" "<<f[p][2]*M_PI<<endl;
		}

		printf("Case #%d: %.7lf\n",tt,M_PI*f[p][k]);
	}
	return 0;
}
