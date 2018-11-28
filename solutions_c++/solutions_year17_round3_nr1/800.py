#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <bitset>
#include <iomanip>
#include <cmath>

# define M_PI           3.14159265358979323846

using namespace std;

typedef long long ll;
typedef pair<string, int> si;
typedef pair<int, int> ii;

const int CMAX = 1e5+10;
const double eps = 1e-7;

struct cake {
	int R, H;
	bool operator<(cake& rhs) {
		return rhs.R < R || rhs.R == R && rhs.H < H;
	}
} cakes[1010];
double dp[1010][1010];

double startA(double R, double H) {

	return R*R + 2 * H*R;

}

double addA(double R, double H) {
	return 2 * H*R;
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG


	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K;
		cin >> N >> K;

		for (int j = 0; j < N; j++) {
			cin >> cakes[j].R >> cakes[j].H;
		}

		sort(cakes, cakes + N);

		for (int cnt = 1; cnt <= K; cnt++) {
			for (int idx = cnt; idx <= N; idx++) {
				if (cnt == 1)
					dp[cnt][idx] = max(dp[cnt][idx - 1], startA(cakes[idx - 1].R, cakes[idx - 1].H));
				else
					dp[cnt][idx] = max(dp[cnt][idx - 1], dp[cnt - 1][idx - 1] + addA(cakes[idx - 1].R, cakes[idx - 1].H));
			}
		}

		cout << "Case #" << i + 1 << ": " << fixed << setprecision(9) << dp[K][N] * M_PI << endl;

	}

	return 0;
}