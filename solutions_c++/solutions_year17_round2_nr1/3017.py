#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		double d;
		int n;
		cin >> d >> n;
		double max_duration = -1.0;
		for (int i = 0; i < n; i++) {
			int k, s;
			cin >> k >> s;
			double duration = (d - k)/s;
			if (duration > max_duration)
				max_duration = duration;
		}
		cout << "Case #" << tc << ": "
			<< fixed << setprecision(6) << (d/max_duration) << endl;
	}
}