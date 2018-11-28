#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>

using namespace std;

void main() {
	size_t testCount;
	cin >> testCount;

	for (size_t i = 0; i < testCount; i++) {
		size_t D, N;
		cin >> D >> N;

		vector<double> useTime(N);
		for (size_t j = 0; j < N; j++) {
			size_t Kj, Sj;
			cin >> Kj >> Sj;

			useTime[j] = (D - Kj)*1. / ((double)Sj);
		}

		sort(useTime.begin(), useTime.end(), [](double a, double b) -> bool {
			return a > b;
		});

		//cout << "Case #" << i + 1 << ": " << 1.*D / useTime[0] << endl;
		fprintf(stdout, "Case #%d: %.6f\n", i + 1, 1.*D / useTime[0]);
	}
}