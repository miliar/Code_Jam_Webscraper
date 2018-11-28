#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<limits.h>

using namespace std;

int main(void) {
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;

	for (int t = 1; t <= T; t++) {
		int N, Q;
		ifs >> N >> Q;
		vector<int> E(N), S(N);
		for (int i = 0; i < N; i++) ifs >> E[i] >> S[i];
		vector<int> D(N);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i + 1 == j) ifs >> D[i];
				else {
					int dummy;
					ifs >> dummy;
				}
			}
		}
		{
			int U, V;
			ifs >> U >> V;
		}
		vector<double> dp(N, DBL_MAX);
		dp[0] = 0.0;
		for (int i = 0; i < N; i++) {
			long long dist = 0;
			for (int j = i + 1; j < N; j++) {
				dist += D[j - 1];
				E[i] -= D[j - 1];
				if (E[i] < 0) break;
				dp[j] = min(dp[j], dp[i] + (double)dist / S[i]);
			}
		}
		cout << "Case #" << t << ": " << fixed << setprecision(10) << dp[N - 1] << endl;
		ofs << "Case #" << t << ": " << fixed << setprecision(10) << dp[N - 1] << endl;
	}

	system("pause");
	return 0;
}