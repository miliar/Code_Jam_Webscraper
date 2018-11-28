#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

double solve() {
	int N, K;
	cin >> N >> K;
	double units;
	cin >> units;

	vector<double> cores(N, 0.0);
	for(int i = 0; i < N; i++) {
		cin >> cores[i];
	}
	sort(cores.begin(), cores.end());

	for(int i = 0; i < N; i++) {
		double dif = (i < N-1) ? (cores[i+1] - cores[i]) : (1 - cores[i]);

		if(units >= dif*(i+1)) {
			for(int j = 0; j <= i; j++) { cores[j] += dif; }
			units -= dif*(i+1);
		}
		else {
			for(int j = 0; j <= i; j++) { cores[j] += units/(double)(i+1); }
			units = 0;
			break;
		}
	}

	double result = 1.0;
	for(int i = 0; i < N; i++) { result *= cores[i]; }

	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		double result = solve();
		cout << "Case #" << (i+1) << ": " << setprecision(8) << result << endl;
	}
	return 0;
}
