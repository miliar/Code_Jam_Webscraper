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
const int N = 106,P=5;

map<pair<pii,pii>,int>M[P];

int get(int r1,int r2,int r3,int m,int p){
	pair<pii,pii> u=make_pair(pii(r1,r2),pii(r3,m));
	if(M[p].find(u)!=M[p].end())return M[p][u];
	int ret=0;
	if(r1)ret=max(ret,(m==0?1:0)+get(r1-1,r2,r3,(m+1)%p,p));
	if(r2)ret=max(ret,(m==0?1:0)+get(r1,r2-1,r3,(m+2)%p,p));
	if(r3)ret=max(ret,(m==0?1:0)+get(r1,r2,r3-1,(m+3)%p,p));
	return M[p][u]=ret;
}
void solve() {
	int n,p;
	scanf("%d%d",&n,&p);
	int r[5];
	r[0]=r[1]=r[2]=r[3]=0;
	fru(i,n){
		int a;
		scanf("%d",&a);
		a%=p;
		r[a]++;
	}
	printf("%d\n",r[0]+get(r[1],r[2],r[3],0,p));
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
