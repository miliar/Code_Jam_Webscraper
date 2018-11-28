// by ξ
// program sky  :)

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
typedef pair<int ,int> PII;
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

int n,P,a[4];

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		printf("Case #%d: ",tc);
		n=IN();P=IN();
		rep(i,0,P)a[i]=0;
		For(i,1,n)++a[IN()%P];
		if(P==2){
			printf("%d\n",a[0]+(a[1]+1>>1));
		}else if(P==3){
			int ans = a[0];
			int tmp = min(a[1],a[2]);
			ans+=tmp;
			a[1]-=tmp;a[2]-=tmp;
			ans+=(a[1]+a[2]+2)/3;
			printf("%d\n",ans);
		}else{
			int ans = a[0];
			ans += a[2]/2;
			a[2]%=2;
			int tmp = min(a[1],a[3]);
			ans+=tmp;
			a[1]-=tmp;
			a[3]-=tmp;
			if(a[1]+a[2]+a[3]>0)ans++;
			printf("%d\n",ans);
		}
	}
// never say goodbye
}