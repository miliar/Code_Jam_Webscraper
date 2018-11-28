#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>

#define f first
#define s second

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int u = 0; u < T; ++u) {
		int d, n;
        double max_t = 0.;
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            int k, s;
            cin >> k >> s;
            double t = 1. * (d - k) / s;
            max_t = max(max_t, t);
        }
        double res = 1. * d / max_t;
        cout.precision(10);
		cout << "Case #" << u + 1 << ": " << fixed << res << "\n";
	}
	return 0;
}