#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int D, N;
		cin >> D >> N;

		double endtime = 0;
		for (int i = 0; i < N; i++) {
			double start, speed;
			cin >> start >> speed;

			double poss = (double(D)-start) / speed;
			if (poss > endtime) endtime = poss;
		}

		cout << "Case #" << t << ": " << setprecision(12) << double(D)/endtime << '\n';
	}

	return 0;
}
