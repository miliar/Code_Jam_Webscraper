#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <list>
#include <array>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

static void solve() {
	int N, K;
	cin >> N >> K;
	vector<pair<long, long>> RH;
	vector<vector<long>> A;

	for (int i = 0; i < N; i++) {
		A.emplace_back(K, 0);
	}

	for (int i = 0; i < N; i++) {
		int Ri, Hi;
		cin >> Ri >> Hi;
		RH.emplace_back(Ri, Hi);
	}

	sort(RH.begin(), RH.end(), [](auto &lhs, auto &rhs) {
		return lhs.first > rhs.first;
	});

	for (int i = 0; i < N; i++) {
		A[i][0] = 2 * RH[i].first * RH[i].second + RH[i].first * RH[i].first;

		if (i > 0) {
			A[i][0] = max(A[i][0], A[i - 1][0]);
		}
	}

	for (int j = 1; j < K; j++) {
		for (int i = j; i < N; i++) {
			A[i][j] = max(A[i - 1][j], A[i - 1][j - 1] + 2 * RH[i].first * RH[i].second);
		}
	}

	printf("%.7lf", double(A[N - 1][K - 1]) * acos(double(-1)));
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
