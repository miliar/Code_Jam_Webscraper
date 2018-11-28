#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<cassert>
#include<queue>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
struct cww{cww(){ios::sync_with_stdio(false);cin.tie(0);}}star;

const int MAX = 111;
int C[MAX], D[MAX];
int J[MAX], K[MAX];

const int INF = 1e5;
int dp[1000][1000][2][2];
int NG[2][1500];

void solve() {
	int AC, AJ;
	cin >> AC >> AJ;
	memset(NG, 0, sizeof(NG));
	// cam は 0
	for (int i = 0; i < AC; i++) {
		cin >> C[i] >> D[i];
		for (int j = C[i]; j < D[i]; j++)
			NG[0][j] = 1;
	}
	// jam は 1
	for (int i = 0; i < AJ; i++) {
		cin >> J[i] >> K[i];
		for (int j = J[i]; j < K[i]; j++)
			NG[1][j] = 1;
	}
	for (int i = 0; i < 1000; i++)
		for (int j = 0; j < 1000; j++)
			for (int k = 0; k < 2; k++)
				for (int l = 0; l < 2; l++)
					dp[i][j][k][l] = INF;

	for (int i = 0; i < 2; i++) 
		if (!NG[i][0]) dp[0][0][i][i] = 0;
	for (int sumT = 0; sumT < 1440; sumT++) {
		for (int cam = 0; cam <= min(sumT, 720); ++cam) {
			int jam = sumT - cam;
			if (jam > 720) continue;
			for (int flag = 0; flag < 2; ++flag) {
				if (cam < 720 && !NG[0][sumT+1]) {
					dp[cam+1][jam][0][flag] = min(dp[cam][jam][0][flag], dp[cam][jam][1][flag] + 1);
					if (cam+jam+1 == 1440 && (0 ^ flag) == 1) {
						++dp[cam+1][jam][0][flag];
					}
				}
				if (jam < 720 && !NG[1][sumT+1]) {
					dp[cam][jam+1][1][flag] = min(dp[cam][jam][0][flag] + 1, dp[cam][jam][1][flag]);
					if (cam+jam+1 == 1440 && (1 ^ flag) == 1) {
						++dp[cam][jam+1][1][flag];
					}
				}
			}
		}
	}
	int ans = INF;
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 2; j++)
			ans = min(ans, dp[720][720][i][j]);

	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
