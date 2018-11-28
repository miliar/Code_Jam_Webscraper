#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pp;
typedef pair<ll,ll> pll;
void read(int& x){ scanf("%d",&x); }
void read(ll& x){ scanf("%lld",&x); }
template<typename T,typename... Args>
void read(T& a,Args&... b){ read(a); read(b...); }
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define x first
#define y second
const int inf = 1e9;

int n, m;
bool na[1500];
bool nb[1500];
int dp[2][2][1500][800];
void work(){
	read(n, m);
	memset(na, 0, sizeof(na));
	memset(nb, 0, sizeof(nb));
	for(int i=1; i<=n; ++i){
		int l, r; read(l, r);
		for(;l<r;++l) na[l]=1;
	}
	for(int i=1; i<=m; ++i){
		int l, r; read(l, r);
		for(;l<r;++l) nb[l]=1;
	}
	memset(dp, 0x7f, sizeof(dp));
	bool* myno[2]={na, nb};
	int ans = inf;
	for(int s=0; s<2; ++s){
		if(myno[s][0]) continue;
		dp[s][s][0][1]=0;
		for(int i=1; i<1440; ++i){
			for(int cur=0; cur<2; ++cur){
				if(myno[cur][i]) continue;
				for(int st=1; st<=720; ++st){
					dp[s][cur][i][st] = min({
						dp[s][cur][i-1][st-(s==cur)],
						dp[s][1-cur][i-1][st-(s==cur)]+1,
					});
				}
			}
		}
		ans = min({ans, dp[s][s][1439][720], dp[s][1-s][1439][720]+1});
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int tc; read(tc);
	for(int i=1; i<=tc; ++i){
		printf("Case #%d: ", i);
		work();
		fprintf(stderr, "Done case %d/%d\n", i, tc);
	}
    return 0;
}
