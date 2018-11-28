#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 2005;
const int MOD = 1000000007;

double PI = acos(-1);

ll dp[MAXN][MAXN];
vector<pair<ll,ll>> v;

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		int n,k; cin >> n >> k;
		for(int i=1;i<=n;i++){
			ll r,h; cin >> r >> h;
			v.push_back({r,h});
		}
		sort(v.begin(),v.end());
		reverse(v.begin(),v.end());
		for(int i=1;i<=n;i++){
			ll r = v[i-1].first , h = v[i-1].second;
			dp[i][1] = r * r + r * h * 2;
			dp[i][1] = max(dp[i-1][1],dp[i][1]);
			for(int j=2;j<=k;j++){
				dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+r*h*2);
			}
		}
		double ans = PI * dp[n][k];
		cout << setprecision(11) << fixed << ans << '\n';
		//clear
		v.clear();
		memset(dp,0,sizeof dp);
	}
	return 0;
}

