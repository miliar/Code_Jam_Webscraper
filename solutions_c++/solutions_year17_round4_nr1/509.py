#include <iostream>
#include <algorithm>
using namespace std;

int counts[4];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, P;
		cin >> N >> P;

		for (int j = 0; j < P; j++) {
			counts[j] = 0;
		}

		for (int i = 0; i < N; i++) {
			int peeps;
			cin >> peeps;

			counts[peeps%P]++;
		}

		if (counts[P-1] > counts[1]) {
			swap(counts[P-1], counts[1]);
		}

		int total = 0;
		for (int j = 0; j < P; j++) {
			total += j * counts[j];
		}

		cout << "Case #" << t << ": " << counts[0]+(total+P-1)/P << '\n';
	}

	return 0;
}
