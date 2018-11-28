#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

double Solve(int D, const vector<int> &K, const vector<int> &S)
{
	double FinishTime = 0;

	for (int i = 0; i < K.size(); i++) {
		FinishTime = std::max(FinishTime, static_cast<double>(D - K[i]) / S[i]);
	}

	return D / FinishTime;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int D, N;
		cin >> D >> N;
		vector<int> K, S;

		for (int j = 0; j < N; j++) {
			int ki, si;
			cin >> ki >> si;
			K.push_back(ki);
			S.push_back(si);
		}

		cout << "Case #" << i << ": ";
		printf("%.6lf", Solve(D, K, S));
		cout << "\n";
	}
	return 0;
}
