#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define fst first
#define snd second
const ll MODP = 1000000007;

ll n, q;
ll e[128], s[128], d[128][128];
ll u[128], v[128];
double dd[128][128];
void solve(void){
	cin >> n >> q;
	for(int i=0;i<n;i++) cin >> e[i] >> s[i];
	for(int i=0;i<n;i++)for(int j=0;j<n;j++) {cin >> d[i][j];}
	for(int i=0;i<q;i++) {cin >> u[i] >> v[i]; u[i]--; v[i]--;}

/*
	ll sd[n]; sd[0] = 0; for(int i=1;i<n;i++) sd[i] = sd[i-1] + d[i-1][i];
	double dp[n]; for(int i=0;i<n;i++) dp[i] = DBL_MAX; dp[0] = 0.0;
	for(int i=1;i<n;i++){
		for(int j=0;j<i;j++){
			if (sd[i]-sd[j] > e[j]) continue;
			dp[i] = min(dp[i], dp[j] + (sd[i]-sd[j]+0.0)/s[j]);
		}
	}
	printf("%.8f\n", dp[n-1]);
*/
	for(int i=0;i<n;i++) d[i][i] = 0;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int k=0;k<n;k++){
				if (d[j][i]==-1 || d[i][k]==-1) continue;
				if (d[j][k]==-1) d[j][k] = d[j][i] + d[i][k];
				else d[j][k] = min(d[j][k], d[j][i] + d[i][k]);
			}
		}
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if (0 <= d[i][j] && d[i][j] <= e[i]) dd[i][j] = (d[i][j]+0.0) / s[i]; else dd[i][j] = -1.0;
		}
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int k=0;k<n;k++){
				if (dd[j][i]==-1.0 || dd[i][k]==-1.0) continue;
				if (dd[j][k]==-1.0) dd[j][k] = dd[j][i] + dd[i][k];
				else dd[j][k] = min(dd[j][k], dd[j][i] + dd[i][k]);
			}
		}
	}

	for(int i=0;i<q;i++){
		printf("%.8f",dd[u[i]][v[i]]);
		if (i+1<q) printf(" ");
	}
	cout << endl;

	return;
}

int main(void){
	int T;
	cin >> T;
	for(int tcnt=1;tcnt<=T;tcnt++){
		cout << "Case #" << tcnt << ": ";
		solve();
	}
	return 0;
}