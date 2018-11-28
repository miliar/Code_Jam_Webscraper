#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <iomanip>

using namespace std;

struct Pancake {
	int64_t r, h;

	bool operator<(const Pancake& rhs) const {
		return r * h > rhs.r * rhs.h;
	}
};

int N, K;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N >> K;
		vector<Pancake> P(N);

		for (int i = 0; i < N; i++) {
			cin >> P[i].r >> P[i].h;
		}

		sort(P.begin(), P.end());
		long double base = 0, ans = 0, lar = 0;
		for (int i = 0; i < K - 1; i++) {
			base += 2 * M_PI * (long double)P[i].r * (long double)P[i].h;
			lar = max(lar, M_PI * (long double)P[i].r * (long double)P[i].r);
		}

		for (int i = K - 1; i < N; i++) {
			ans = max(ans, base + max(lar, M_PI * (long double)P[i].r * (long double)P[i].r) + 2 * M_PI * (long double)P[i].r * (long double)P[i].h);
		}

		cout << "Case #" << t << ": " << setprecision(20) << ans << endl;
	}

	return 0;
}