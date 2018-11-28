#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<limits.h>
#include<fstream>

using namespace std;

int main(void) {
	ifstream ifs("C-small-1-attempt0 (1).in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	for(int t = 1; t <= T; t++){
		int N, K;
		ifs >> N >> K;
		double U;
		ifs >> U;
		vector<double> P(N);
		for (int i = 0; i < N; i++) ifs >> P[i];

		sort(P.begin(), P.end());
		P.push_back(1.0);
		for (int i = 0; i < N && U > 0; i++) {
			double diff;
			diff = P[i + 1] - P[i];
			diff = min(diff, U / (i + 1));
			for (int j = 0; j <= i; j++) P[j] += diff;
			U -= diff * (i + 1);
		}

		double ans = 1;
		for (int i = 0; i < N; i++) ans *= P[i];

		cout << "Case #" << t << ": " << ans << endl;
		ofs << "Case #" << t << ": " << fixed << setprecision(10) << ans << endl;
	}

	return 0;
}