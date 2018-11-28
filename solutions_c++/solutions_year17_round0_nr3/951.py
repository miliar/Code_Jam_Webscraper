// by ξ
// program sky  :)

#include <map>
#include <vector>
#include <complex>
#include <stdio.h>
#include <cassert>
#include <algorithm>

#define Rin register int
#define oo (c=getchar())
#define For(i,l,r) for(int _r=r,i=l;i<=_r;++i)
#define rep(i,l,r) for(int _r=r,i=l;i<_r;++i)
#define dto(i,r,l) for(int _l=l,i=r;i>=_l;--i)
#define ALL(V) V.begin(),V.end()
#define SZ(A) (int(A.size()))
#define pb push_back
#define mk make_pair
#define x first
#define y second

using namespace std;

typedef double db;
typedef long long LL;
typedef pair<LL ,LL> PII;
typedef complex<db> cpx;
typedef vector<int> VI;
typedef vector<PII> VII;

inline int IN(){
	char c;Rin x=0;
	for(;oo<48 && c^'-' || c>57;);bool f=c=='-';if(f)oo;
	for(;c>47 && c<58;oo)x=(x<<3)+(x<<1)+c-48;if(f)x=-x;return x;
}

inline void hello(){
	freopen("ha.in","r",stdin);
//	freopen("ha.out","w",stdout);
}

LL n,m;

map<LL,LL> Maps;

inline PII han(LL x){
	return {x-1>>1,x>>1};
}

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		printf("Case #%d: ",tc);
		scanf("%lld %lld",&n,&m);
		Maps.clear();
		Maps[n]=1;
		for(;;){
			PII it = *Maps.rbegin();
			Maps.erase(it.x);
			if(it.y>=m){
				PII tmp = han(it.x);
				printf("%lld %lld\n",tmp.y,tmp.x);
				break;
			}
			PII tmp = han(it.x);
			Maps[tmp.x]+=it.y;
			Maps[tmp.y]+=it.y;
			m-=it.y;
		}
	}
// never say goodbye
}
