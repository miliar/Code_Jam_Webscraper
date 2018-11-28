#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <iomanip>

using namespace std;


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, P;
		cin >> N >> P;

		int ms[4]{0};
		for (int i = 0; i < N; i++) {
			int G;
			cin >> G;
			ms[G % P]++;
		}

		int ans = 0;
		if (P == 2) {
			ans = ms[0] + ms[1] / 2;
			if (ms[1] % 2 == 1) ans++;
		} else if (P == 3) {
			int v = min(ms[1], ms[2]);
			ans = ms[0] + v;
			ms[1] -= v;
			ms[2] -= v;
			ans += ms[1] / 3;
			ans += ms[2] / 3;
			if (ms[1] % 3 != 0 || ms[2] % 3 != 0) {
				ans++;
			}
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}