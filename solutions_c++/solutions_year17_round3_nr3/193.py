#include <algorithm>
#include <iomanip>
#include <vector>
#include <iostream>

using namespace std;

int n, k;
const int N = 100;
double dp[N][N];
const double EPS = 1e-9;

double calc(vector <double> const & p) {
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= n; j++) {
			dp[i][j] = 0;
		}
	}
	dp[0][0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= n; j++) {
			dp[i + 1][j + 1] += dp[i][j] * p[i];
			dp[i + 1][j] += dp[i][j] * (1.0 - p[i]);
		}
	}
	double rt = 0;
	for (int i = k; i <= n; i++) {
		rt += dp[n][i];
	}
	return rt;
} 

void solve() {
	cin >> n >> k;
	double U;
	cin >> U;
	vector <double> p(n);
	
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}

	sort(p.begin(), p.end());
	
	for (int i = 0; i < n - 1; i++) {
		double diff = p[i + 1] - p[i];
		double each = min(diff, U / (i + 1));
		U = max(0.0, U - diff * (i + 1));
		for (int j = 0; j <= i; j++) {
			p[j] += each;
		}
		if (U < EPS) break;
	}
	if (U > 0) {
		double each = U / n;
		for (int i = 0; i < n; i++) {
			p[i] += each;
		}
	}
	cout << fixed << setprecision(10) << calc(p) << "\n";
}

int main() {

	int ts;
	cin >> ts;
	for (int i = 1; i <= ts; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}