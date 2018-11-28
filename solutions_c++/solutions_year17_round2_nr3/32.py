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

int n,Q,lim[111],V[111];
LL d[111][111];
db f[111][111];

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		printf("Case #%d:",tc);
		n=IN();Q=IN();
		For(i,1,n){
			lim[i]=IN();
			V[i]=IN();
		}
		For(i,1,n)For(j,1,n){
			d[i][j]=IN();
		}
		For(k,1,n)For(i,1,n)For(j,1,n){
			if(~d[i][k] && ~d[k][j]){
				if(d[i][j]<0)d[i][j]=d[i][k]+d[k][j];
				else d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
			}
		}
		For(i,1,n)For(j,1,n){
			f[i][j]=i==j?0:d[i][j]<=lim[i]?d[i][j]*1./V[i]:-1;
		}
		For(k,1,n)For(i,1,n)For(j,1,n){
			if(f[i][k]>=0 && f[k][j]>=0){
				if(f[i][j]<0)f[i][j]=f[i][k]+f[k][j];
				else f[i][j]=min(f[i][j],f[i][k]+f[k][j]);
			}
		}
		For(i,1,Q){
			int u=IN(),v=IN();
			printf(" %.8lf",f[u][v]);
		}
		puts("");
	}
// never say goodbye
}