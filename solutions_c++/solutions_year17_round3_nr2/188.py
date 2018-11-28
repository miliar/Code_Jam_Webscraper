#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		vector<bool> can[2]; can[0] = can[1] = vector<bool> (1440, true);
		int nA, nB; cin >> nA >> nB;
		for (int i=0; i<nA; i++) {
			int l, r; cin >> l >> r;
			for (int t=l; t<r; t++) can[0][t] = false;
		}
		for (int i=0; i<nB; i++) {
			int l, r; cin >> l >> r;
			for (int t=l; t<r; t++) can[1][t] = false;
		}
		int answer = 1e9;
		for (int start=0; start<2; start++) {
			static int dp[2][721];
			for (int i=0;i<2;i++)for(int t=0;t<=720;t++)dp[i][t]=1e9;
			dp[start][0] = 0;
			for (int t=0; t<1440; t++) {
				static int dp2[2][721];
				for(int at=0;at<=720;at++){
					dp2[0][at] = dp2[1][at] = 1e9;
					if (at > 0 && can[0][t]) dp2[0][at] = min(dp[0][at-1], dp[1][at-1] + 1);
					if (can[1][t]) dp2[1][at] = min(dp[1][at], dp[0][at] + 1);
				}
				memcpy(dp, dp2, sizeof dp2);
			}
			answer = min(answer, min(dp[start][720], dp[1-start][720] + 1));
		}
		printf("Case #%d: %d\n", tc, answer);
	}
}
