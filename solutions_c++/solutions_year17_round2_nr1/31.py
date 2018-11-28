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

int n,D,pos[100010],V[100010];
db T[100010];

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		D=IN();
		n=IN();
		For(i,1,n)pos[i]=IN(),V[i]=IN();
		dto(i,n,1){
			T[i]=1.*(D-pos[i])/V[i];
			if(i<n && T[i+1]>T[i])T[i]=T[i+1];
		}
		printf("Case #%d: %lf\n",tc,D/T[1]);
	}
// never say goodbye
}