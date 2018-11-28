#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 105;

bool used_states[MAX_N][MAX_N];
int n, e[MAX_N], s[MAX_N], a[MAX_N][MAX_N];
double dp[MAX_N][MAX_N];

double solve(int node, int horse, int rem, int speed) {
	if(node == n) {
		return 0;
	}
	else if(used_states[node][horse]) {
		return dp[node][horse];
	}

	double ans;
	if(rem - a[node][node + 1] < 0) {
		ans = solve(node + 1, node, e[node] - a[node][node + 1], s[node]) + a[node][node + 1] / (double) s[node];
	}
	else {
		ans = solve(node + 1, horse, rem - a[node][node + 1], speed) + a[node][node + 1] / (double) speed;
		ans = min(ans, solve(node + 1, node, e[node] - a[node][node + 1], s[node]) + a[node][node + 1] / (double) s[node]);
	}

	dp[node][horse] = ans;
	used_states[node][horse] = true;
	
	return ans;
}

int main() {
	int cnt_tests;
	scanf("%d", &cnt_tests);

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int q;
		scanf("%d%d", &n, &q);
	
		for(int i = 1; i <= n; i++) {
			scanf("%d%d", &e[i], &s[i]);
		}

		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		
		for(int i = 0; i < q; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
		}

		memset(used_states, 0, sizeof(used_states));
		printf("Case #%d: %.8f\n", cs, solve(1, 1, e[1], s[1]));
	}

	return 0;
}
