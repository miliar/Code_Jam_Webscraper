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

struct bip{
	int n,res,bx[555],by[555],mat[555][555],weix[555],weiy[555];
	bool vis[555],ok[555][555];
	int* operator [] (int x){
		return mat[x];
	}
	void ins(int x,int y){
		weix[x]=1;weiy[y]=1;
		mat[x][y]=1;
		++res;
	}
	bool gao(int u){
		if(vis[u])return 0;
		vis[u]=1;
		assert(!weix[u]);
		For(v,1,n)if(ok[u][v])
			if(!by[v] || gao(by[v]))return by[v]=u , bx[u]=v, 1;
		return 0;
	}
	int suan(){
		For(i,1,n)For(j,1,n)ok[i][j] = ok[i][j] && !weix[i] && !weiy[j];
		For(i,1,n)if(!weix[i]){
			For(j,1,n)vis[j]=0;
			res+=gao(i);
		}
		For(i,1,n)mat[i][bx[i]] = 1;
		return res;
	}
	void reset(){
		res=0;
		For(i,1,n)bx[i]=by[i]=weix[i]=weiy[i]=0;
		For(i,1,n)For(j,1,n)mat[i][j]=ok[i][j]=0;
		n=0;
	}
}xie,shu;

int n,m;
char A[555][555],B[555][555];

inline void reset_all(){
	For(i,1,n)For(j,1,n)A[i][j]=B[i][j]=0;
	xie.reset();
	shu.reset();
}

int main(){
// say hello
	hello();
	For(tc,1,IN()){
		n=IN();m=IN();
		int res=0;
		shu.n=n;
		xie.n=n*2-1;
		For(i,1,n)For(j,1,n)shu.ok[i][j]=1,xie.ok[i+j-1][i-j+n]=1;
		For(i,1,m){
			char c;
			for(;oo^'+' && c^'x' && c^'o';);
			int x = IN(),y = IN();
			if(c=='o' || c=='+')xie.ins(x+y-1,x-y+n);
			if(c=='o' || c=='x')shu.ins(x,y);
			A[x][y]=c;
		}
		res += xie.suan();
		res += shu.suan();
		For(i,1,n)For(j,1,n)if(xie[i+j-1][i-j+n])B[i][j] = '+';
		For(i,1,n)For(j,1,n)if(shu[i][j])B[i][j] = B[i][j]=='+'?'o':'x';
		int num = 0;
		For(i,1,n)For(j,1,n)if(A[i][j]^B[i][j])++num;
		printf("Case #%d: %d %d\n",tc,res,num);
		For(i,1,n)For(j,1,n)if(A[i][j]^B[i][j])printf("%c %d %d\n",B[i][j],i,j);
		reset_all();
	}
// never say goodbye
}
