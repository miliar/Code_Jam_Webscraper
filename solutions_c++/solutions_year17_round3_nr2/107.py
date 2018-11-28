#include<iostream>
#include<vector>
#include<algorithm>
#define INF 1000000000
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		int n, m;
		cin >> n >> m;
		
		vector<bool> avail[2] = {vector<bool>(1440, true), vector<bool>(1440, true)};
		
		for(int i=0;i<n;i++) {
			int l, r;
			cin >> l >> r;
			
			while(l < r)
				avail[0][l++] = false;
		}
		
		for(int i=0;i<m;i++) {
			int l, r;
			cin >> l >> r;
			
			while(l < r)
				avail[1][l++] = false;
		}
		
		static int dp[1441][1441][2][2];
		fill(dp[0][0][0], dp[0][0][0] + 1441 * 1441 * 2 * 2, INF);
		dp[0][0][0][0] = 0;
		dp[0][0][1][1] = 0;
		
		for(int t = 0; t < 1440; t++) {
			for(int i=0;i<=t;i++)
				for(int start = 0; start < 2; start++)
					for(int side = 0; side < 2; side++)
						for(int nside = 0; nside < 2; nside++) if(avail[nside][t])
							dp[t+1][i+nside][start][nside] = min(dp[t+1][i+nside][start][nside],
																 dp[t][i][start][side] + (nside != side) );
		}
		
		int result = INF;
		for(int start = 0; start < 2; start++)
			for(int side = 0; side < 2; side++)
				result = min(result, dp[1440][720][start][side] + (side != start) );
				
		cout << "Case #" << TCASE << ": " << result << '\n';
	}
	
	return 0;
}

