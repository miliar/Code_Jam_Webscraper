#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N = 100010;
int v[N];
int n, p;
int dp[110][110][110], cnt, vis[110][110][110];
int solveFour (int m1, int m2, int m3) {
	if (m1 < 0 or m2 < 0 or m3 < 0) return 0;
	if (m1 == 0 and m2 == 0 and m3 == 0) return 0;
	if (vis[m1][m2][m3] == cnt) return dp[m1][m2][m3];
	vis[m1][m2][m3] = cnt;
	int ret = 1;
	for (int i = 0; i <= 4; i++) {
		for (int j = 0; j <= 4; j++) {
			for (int k = 0; k <= 4; k++) {
				if (!i and !j and !k) continue;
				int mod = i + j*2 + k*3;
				if (mod % 4) continue;
				ret = max(ret, solveFour(m1-i, m2-j, m3-k) + 1);
			}
		}
	}
	return dp[m1][m2][m3] = ret;
}
int solveTwo () {
	int par = 0, impar = 0;
	for (int i = 0; i < n; i++) {
		if (v[i] % 2) impar++;
		else par++;
	}
	return par + (impar + 1) / 2;
}
int solveThree (int m1, int m2) {
	if (m1 < 0 or m2 < 0) return 0;
	if (m1 == 0 and m2 == 0) return 0;
	if (vis[m1][m2][0] == cnt) return dp[m1][m2][0];
	vis[m1][m2][0] = cnt;

	int ret = 1;
	for (int i = 0; i <= 3; i++) {
		for (int j = 0; j <= 3; j++) {
			if (!i and !j) continue;
			int mod = i + j*2;
			if (mod % 3) continue;
			ret = max(ret, solveThree(m1-i, m2-j) + 1);
		}
	}
	return dp[m1][m2][0] = ret;
}
int solveThree () {
	int m0 = 0, m1 = 0, m2 = 0;
	for (int i = 0; i < n; i++) {
		if (v[i] % 3 == 0) m0++;
		else if (v[i] % 3 == 1) m1++;
		else m2++;
	}
	return m0 + solveThree (m1, m2);
}
int solveFour() {
	int m0 = 0, m1 = 0, m2 = 0, m3 = 0;
	for (int i = 0; i < n; i++) {
		if (v[i] % 4 == 0) m0++;
		else if (v[i] % 4 == 1) m1++;
		else if (v[i] % 4 == 2) m2++;
		else m3++;
	}
	return m0 + solveFour (m1, m2, m3);
}
int main (void) {
	int t; scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++) {
			scanf("%d", v + i);
		}
		int ans = 0;
		cnt++;
		if (p == 2) ans = solveTwo();
		else if (p == 3) ans = solveThree();
		else ans = solveFour();

		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}

