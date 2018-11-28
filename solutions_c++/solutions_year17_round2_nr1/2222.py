#include <iomanip>
#include <iostream>
using namespace std;

int main() {
	int T;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cout << "Case #" << t << ": ";

		long double d, n;

		cin >> d >> n;

		long double timer = 0;
		long double pos, speed;
		for (int i=0 ; i<n ; ++i) {
			cin >> pos >> speed;
			timer = max(timer, (d - pos) / speed);
		}

		cout << fixed << setprecision(6) << d / timer << endl;
	}

	return 0;
}