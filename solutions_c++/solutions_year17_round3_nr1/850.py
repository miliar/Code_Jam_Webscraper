#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<limits.h>
#include<fstream>

#define PI 3.141592653589793238

using namespace std;

struct pancake {
	double R, H, S;
};

bool operator<(struct pancake& lhs, struct pancake& rhs) {
	return lhs.R < rhs.R;
}

int main(void) {
	ifstream ifs("A-large (1).in");
	ofstream ofs("out.txt");

	int T;
	ifs >> T;
	for (int t = 1; t <= T; t++) {
		int K, N;
		ifs >> N >> K;
		vector<struct pancake> P(N);
		for (int i = 0; i < N; i++) {
			ifs >> P[i].R >> P[i].H;
			P[i].S = 2.0 * PI * P[i].R * P[i].H;
		}
		sort(P.rbegin(), P.rend());
		double ans = 0;
		for (int i = 0; i + K <= N; i++) {
			vector<double> S;
			for (int j = i + 1; j < N; j++) {
				S.push_back(P[j].S);
			}
			sort(S.rbegin(), S.rend());
			double ans_temp = 0;
			ans_temp += P[i].S + PI * P[i].R * P[i].R;
			for (int j = 0; j < K - 1; j++) ans_temp += S[j];
			ans = max(ans, ans_temp);
		}
		cout << "Case #" << t << ": " << fixed << setprecision(10) << ans << endl;
		ofs << "Case #" << t << ": " << fixed << setprecision(10) << ans << endl;
	}
	system("pause");
	return 0;
}
