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

const ll inft = 1LL<<60;
const int mod = 1000000007;
const int MAXN = 106;
const double din=1e16;

ll E[MAXN],S[MAXN];
ll T[MAXN][MAXN];
D R[MAXN][MAXN];
void solve() {
	int n,q;
	scanf("%d%d",&n,&q);
	fru(i,n)scanf("%lld%lld",&E[i],&S[i]);
	fru(i,n)fru(j,n)scanf("%lld",&T[i][j]);
	fru(i,n)fru(j,n)if(T[i][j]==-1)T[i][j]=inft;
	fru(i,n)T[i][i]=0;
	//floyd war
	fru(k,n)fru(i,n)fru(j,n)if(T[i][j]>T[i][k]+T[k][j])T[i][j]=T[i][k]+T[k][j];
	//R
	fru(i,n)fru(j,n)if(T[i][j]>E[i])R[i][j]=din;
	else R[i][j]=1.*T[i][j]/S[i];
if(0)	fru(i,n){
		fru(j,n)printf("%.2lf ",R[i][j]);puts("");
	}
	//floyd war
	fru(k,n)fru(i,n)fru(j,n)if(R[i][j]>R[i][k]+R[k][j])R[i][j]=R[i][k]+R[k][j];
	fru(_,q){
		int a,b;
		scanf("%d%d",&a,&b);
		a--;b--;
		assert(R[a][b]<din);
		printf("%.6lf%c",R[a][b],_==q-1?'\n':' ');
	}
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
