#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <list>
#include <array>
#include <map>
#include <algorithm>
using namespace std;

static void solve() {
	int N, K;
	cin >> N >> K;
	double U;
	cin >> U;
	vector<double> P(N);
	for (auto &Pi : P) {
		cin >> Pi;
	}
	sort(P.begin(), P.end());
	for (int i = 0; i < P.size(); i++) {
		double higherP = (i + 1 < P.size() ? P[i + 1] : 1.0);
		if (U >= (i + 1) * (higherP - P[i])) {
			U -= (i + 1) * (higherP - P[i]);
			for (int j = 0; j <= i; j++) {
				P[j] = higherP;
			}
		} else {
			double inc = (U) / (i + 1);
			for (int j = 0; j <= i; j++) {
				P[j] += inc;
			}
			break;
		}
	}

	double accP = 1;
	for (auto &Pi : P) {
		accP *= Pi;
	}

	printf("%.7f", accP);
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
