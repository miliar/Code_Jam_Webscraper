#include <bits/stdc++.h>
using namespace std;

#define pb push_back
typedef pair<int,int> Pair;
typedef long long ll;

double newmin(double a, double b) {
	if (a == -1) return b;
	if (b == -1) return a;
	return (a < b) ? a : b;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	
	cout << fixed << setprecision(10);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cout << "Case #" << tt << ": ";
		int num, q;
		cin >> num >> q;
		int a, b;
		vector<pair<int,int>> horse; horse.pb(Pair(0,0));
		vector<ll> dist; dist.pb(0); dist.pb(0);
		ll dsum = 0;
		for (int i = 0; i < num; i++) {
			cin >> a >> b;
			horse.pb(Pair(a,b));
		}
		//cerr << "read horses" << endl;
		for (int i = 0; i < num; i++) {
			for (int j = 0; j < num; j++) {
				cin >> a;
				if (a != -1) {
					dsum += a;
					dist.pb(dsum);
				}
			}
		}
		//cerr << "read matrix" << endl;
		// query
		cin >> a >> b;
		//cerr << "read query" << endl;
		//
		//cerr << "horse" << endl;
		//for (auto &it : horse)
			//cerr << it.first << " " << it.second << endl;
		//cerr << "dist" << endl;
		//for (auto &it : dist)
			//cerr << it << endl;
		double dp[num+1][num+1]; // [j][horse] := time to j using ith horse
		double ans[num+1];
		for (int i = 0; i <= num; i++) {
			for (int j = 0; j <= num; j++)
				dp[i][j] = -1;
		}
		ans[0] = ans[1] = 0;
		dp[1][1] = 0;
		double tempmin;
		for (int city = 2; city <= num; city++) {
			for (int hor = 1; hor < city; hor++) {
				if (horse[hor].first < dist[city]-dist[hor])
					continue;
				dp[city][hor] = newmin(dp[city][hor], ans[hor] + (double)(dist[city]-dist[hor])/horse[hor].second);
				//cerr << "dp[" << city << "][" << hor << "] = " << dp[city][hor] << endl;
			}
			tempmin = -1;
			for (int i = 1; i <= num; i++)
				tempmin = newmin(tempmin, dp[city][i]);
			ans[city] = tempmin;
		}
		cout << ans[num] << endl;
	}
	return 0;
}
