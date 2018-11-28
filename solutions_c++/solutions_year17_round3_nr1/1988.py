#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long lld;

const int maxn = 1000 + 10;
const long double pi = 3.1415926535897932;

int T, N, K;
struct RH { lld R, H, A; } arr[maxn];
lld dp[maxn][2];

int main()
{
	freopen("A-small-attempt6.in", "r", stdin);
	freopen("A-small-attempt6.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	for (int now_case = 1; now_case <= T; ++now_case) {
		cin >> N >> K;
		for (int i = 0; i < N; ++i) {
			cin >> arr[i].R >> arr[i].H;
			arr[i].A = arr[i].R * arr[i].H * 2;
			arr[i].R *= arr[i].R;
		}
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i < N; ++i) {
			for (int j = K; j > 1; --j) {
				if (dp[j - 1] == 0) continue;
				lld r = max(dp[j - 1][1], arr[i].R);
				lld tmp = dp[j - 1][0] + arr[i].A + r - dp[j - 1][1];
				if (dp[j][0] < tmp) dp[j][0] = tmp, dp[j][1] = r;
			}
			lld tmp = arr[i].A + arr[i].R;
			if (dp[1][0] < tmp) dp[1][0] = tmp, dp[1][1] = arr[i].R;
		}
		cout << "Case #" << now_case << ": " << fixed << setprecision(9) << ((long double)dp[K][0] * pi) << endl;
	}
	return 0;
}
