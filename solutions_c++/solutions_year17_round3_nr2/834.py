#include <bits/stdc++.h>

using namespace std;

#define FOE(i, s, t) for (int i = s; i <= t; i++)
#define FOD(i, s, t) for (int i = s; i >= t; i--)
#define FOR(i, s, t) for (int i = s; i < t; i++)
#define mp make_pair
#define pb push_back
#define LL long long

#define last 1440
#define half 720

int dp[2001][2001][2][2];

int t;

int n, m;
int a[2001];

int ok(int player, int dir){
	if (player == 0 && a[dir] == -1) return false;
	if (player == 1 && a[dir] == 1) return false;
	return true;
}

void solve(){
	scanf("%d%d", &n, &m);
	FOE(i, 0, 1440) a[i] = 0;
	FOE(i, 1, n){
		int s, t; scanf("%d%d", &s, &t);
		FOE(j, s, t - 1) a[j] = -1;
	}

	FOE(i, 1, m){
		int s, t; scanf("%d%d", &s, &t);
		FOE(j, s, t - 1) a[j] = 1;
	}

	int sol = 9999999;
	FOE(i, 0, last) FOE(j, 0, 720) FOE(k, 0, 1) FOE(l, 0, 1) dp[i][j][k][l] = 9999999;
	if (a[0] != -1){
		dp[0][0][0][0] = 0;
	}
	if (a[0] != 1){
		dp[0][1][1][1] = 0;
	}

	FOE(i, 0, last - 2) FOE(j, 0, half) FOE(k, 0, 1) FOE(l, 0, 1){
		int used = i + 1 - j;
		if (ok(k, i)){
			dp[i + 1][j][0][l] = min(dp[i + 1][j][0][l], dp[i][j][k][l] + (k != 0));
			dp[i + 1][j + 1][1][l] = min(dp[i + 1][j + 1][1][l], dp[i][j][k][l] + (k != 1));
		}
	}

//	FOE(i, 0, 1) cout << dp[1159][440][i][1] << endl;
//	FOE(i, 0, 1) cout << dp[1439][719][i][1] << endl;
//	FOE(i, 0, 1) printf("dp[1159][440][%d][1] = %d\n", i, dp[1159][440][i][1]);

	FOE(j, 0, 1) FOE(k, 0, 1) if (ok(j, last)){
		sol = min(sol, dp[last - 1][half][j][k] + (j != k));
	}

	printf("%d\n", sol);
}

int main(){
	scanf("%d", &t);
	FOE(i, 1, t){
		printf("Case #%d: ", i);
		solve();
	}
}
