#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int N = 800;
int dp[N][N][2][2];
int T[N << 1];
int A[2];

int solve(int c, int j, int curr, int start) {
	int &ans = dp[c][j][curr][start];
	if(T[c + j] == curr) {
		return ans = INF;
	}
	if(c == 720 && j == 720) {
		return ans = curr == start ? 0 : 1;
	} 
	if(c > 720 || j > 720) {
		return ans = INF;
	}
	if(ans != -1) {
		return ans;
	}
	ans = INF;
	ans = min(ans, solve(c + 1, j, 0, start) + (curr == 1));
	ans = min(ans, solve(c, j + 1, 1, start) + (curr == 0));
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		scanf("%d %d", A + 0, A + 1);
		memset(T, -1, sizeof T);
		for(int b = 0; b <= 1; ++b) {
			for(int i = 1; i <= A[b]; ++i) {
				int st, en;
				scanf("%d %d", &st, &en);
				for(int j = st; j < en; ++j) {
					T[j] = b;
				}
			}
		}
		T[1440] = T[0];	
		memset(dp, -1, sizeof dp);
		int ans = min(solve(1, 0, 0, 0), solve(0, 1, 1, 1));
		printf("Case #%d: %d\n", tc, ans);
	}
}