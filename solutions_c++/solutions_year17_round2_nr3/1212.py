#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

ll e[100], s[100];
int n, q; 
double mem[100][100];
ll mm[100][100];
ll a[100][100];

double dp(int cur, int hor, ll dis) {
	if (cur == n-1) {
		return 0;
	}
	if (mm[cur][hor] != -1) {
		return mem[cur][hor];
	}
	double time = a[cur][cur+1] * 1.0 / s[hor];
	double add = 1e13;
	if (e[hor] - dis - a[cur][cur+1] >= a[cur+1][cur+2]) {
		add = min(add, dp(cur+1, hor, dis + a[cur][cur+1]));
	}
	add = min(add, dp(cur+1, cur+1, 0));
	mm[cur][hor] = 1;
	//cout << add << endl;
	mem[cur][hor] = time + add;
	// cout << cur << " " << hor << " = " << time + add << " x " << time << endl;
	return mem[cur][hor];
}

int main() {
	int tt; cin >> tt;
	for (int t = 1; t <= tt; t++) {
		cin >> n >> q;
		memset(mm, -1, sizeof mm);
		for (int i = 0; i < n; i++) {
			cin >> e[i] >> s[i];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> a[i][j];
			}
		}
		int u[q], v[q];
		for (int i = 0; i < q; i++) {
			cin >> u[i] >> v[i];
		}
		double ans = dp(0, 0, 0);
		printf("Case #%d: %.6lf\n", t, ans);
	}
}