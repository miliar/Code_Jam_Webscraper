// ayy
// ' lamo
#include <bits/stdc++.h>
#include <bits/extc++.h>
using namespace std;
using namespace __gnu_pbds;
typedef long long ll;
typedef long double ld; //CARE
typedef complex<ld> pt;
#define fi first
#define se second
#define pb push_back
const ld eps=1e-8;
const int inf=1e9+99;
const ll linf=1e18+99;
const int P=1e9+7;

const int N=102;
int p,n,gg[N],c[5];
int dp[4][N][N][N][N];
bool seen[4][N][N][N][N];

bool z(int x) { return !x || x==N-1; }
int g(int x,int a,int b,int c,int d) {
	int &ans=dp[x][a][b][c][d];
	if(seen[x][a][b][c][d]) return ans;
	seen[x][a][b][c][d]=1;
	if(z(a) && z(b) && z(c) && z(d)) return 0;
	ans=0;
	if(!z(a)) ans=max(ans,g(x,a-1,b,c,d));
	if(!z(b)) ans=max(ans,g((x+1)%p,a,b-1,c,d));
	if(!z(c)) ans=max(ans,g((x+2)%p,a,b,c-1,d));
	if(!z(d)) ans=max(ans,g((x+3)%p,a,b,c,d-1));
	if(!x) ++ans;
	return ans;
}


void _m(int t) {
	scanf("%d%d",&n,&p);
	for(int i=0;i<n;i++) scanf("%d",gg+i);
	for(int i=0;i<n;i++) gg[i]%=p;
	sort(gg,gg+n);
	for(int i=0;i<p;i++) c[i]=0;
	for(int i=0;i<n;i++) c[gg[i]]++;
	for(int i=p;i<4;i++) c[i]=N-1;
	int ans=g(0,c[0],c[1],c[2],c[3]);
	printf("Case #%d: %d\n",t,ans);
}



int32_t main() {
	int T; scanf("%d",&T); for(int t=1;t<=T;t++) _m(t);
}










