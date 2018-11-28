#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <iomanip>

using namespace std;

double calcSpeed(int D, int N, vector<int> pos, vector<int> speed) {
	// Find slowest
	double bottleTime = 0;
	for(int i = 0; i < N; i++) {
		bottleTime = max(bottleTime, (double) (D-pos[i]) / (double) speed[i]);
	}
	return ((double)D / bottleTime);
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		int D, N;
		cin >> D >> N;
		vector<int> pos(N);
		vector<int> speed(N);
		for(int j = 0; j < N; j++) {
			cin >> pos[j] >> speed[j];
		}

		double result = calcSpeed(D, N, pos, speed);
		cout << "Case #" << (i+1) << ": ";
		cout << setprecision(8) << result << endl;
	}
	return 0;
}
