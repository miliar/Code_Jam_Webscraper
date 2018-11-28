#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define V  vector
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long
const double pi = 2*acos(0);

vector < pair < double , double > > v;
int n,k;
double dp[2][1005][1005];
void reset(int pos){
	for(int i = 0 ; i <= n ; i++){
		for(int j = 0 ; j<= n ; j++){
			dp[pos][i][j] = 0.00;
		}
	}
}
double solve(){
	reset(0);
	reset(1);
	int now = 0;
	int nxt = 1;
	dp[0][0][0] = 0.0;
	for(int i = 1 ; i<= n ; i++){
		reset(nxt);
		for(int cnt = 0 ; cnt < k ; cnt++) {
			for(int last = 0 ; last < i ; last++){
				if(cnt == 0){
					dp[nxt][cnt+1][i] = max(dp[now][cnt+1][last],pi * v[i-1].first*v[i-1].first + 2*pi*v[i-1].first*v[i-1].second);
				}
				else {
					dp[nxt][cnt+1][i] = max(dp[now][cnt+1][last],dp[now][cnt][last]-pi*v[i-1].first*v[i-1].first + 2*pi*v[i-1].first*v[i-1].second + pi * v[i-1].first * v[i-1].first);
				}
			}
		}
		swap(now,nxt);
	}
	double ans = 0.00;
	for(int last = 1 ; last <= n ; last++) {
		ans = max(ans,dp[now][k][last]);
	}
	return ans;
}
int cs = 0;
int main() {
	int t;
	cin >> t;
	while(t--){
		v.clear();
		cin >> n >> k;
		for(int i = 0 ; i < n ; i++){
			double x, y;
			cin >> x >> y;
			v.push_back(make_pair(x,y));
		}
		sort(v.rbegin(),v.rend());
		printf("Case #%d: %.17lf\n",++cs,solve());
	}
}