#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

struct Horse {
	int k, s;

	Horse() {}
	Horse(int k, int s) : k(k), s(s) {}
};

int t, n, d, cnt = 1;
double ans, tmp, k, s;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> t;

	while (t--) {
		cin >> d >> n;

		ans = tmp = -1.0;		

		for (int i = 0; i < n; ++i) {
			cin >> k >> s;
			tmp = (d - k) / s;
			ans = (tmp > ans) ? tmp : ans;
		}

		ans = d / ans;

		cout << "Case #" << cnt++ << ": ";
		cout << fixed << setprecision(6) << ans << endl;

	}

	return 0;
}
