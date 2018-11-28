#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int ti = 1; ti <= t; ti++) {
		double d;
		int n;
		cin >> d >> n;

		double time = 0.0;

		for (int i = 0; i < n; i++) {
			double k, s;
			cin >> k >> s;

			double ctime = (d - k) / s;

			time = max(time, ctime);
		}

		double speed = d / time;

		cout << "Case #" << ti << ": "
		     << fixed << setprecision(6) << speed << endl;
	}
}
