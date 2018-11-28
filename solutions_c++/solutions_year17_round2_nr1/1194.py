#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int i = 1; i <= nCases; i++) {
		int D, N;
		cin >> D >> N;
		double longest = 0.0;

		for (int k = 0; k < N; k++) {
			int pos, speed;
			cin >> pos >> speed;

			double times = double(D - pos) / speed;
			longest = max(longest, times);
		}

		cout << fixed << setprecision(8);
		cout << "Case #" << i << ": " << D / longest << endl;
	}

	return 0;
}
