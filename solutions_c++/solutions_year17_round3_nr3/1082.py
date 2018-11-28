// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const double zero = 0.000001;

double solve(int N, int K, double U, vector<double> P)
{
	if (N == 1) {
		return P[0] + U;
	}

	sort(P.begin(), P.end());
	int min = 0;
	double u = U;
	while (true) {
		if (min == N-1) {
			auto ui = u / N;
			for (int i = 0; i < N; i++) {
				P[i] += ui;
			}
			break;
		}
		double diff = P[min + 1] - P[min];
		if (diff > zero) {
			if (diff*(min + 1) + zero > u) {
				auto ui = u / (min + 1);
				for (int i = min; i >= 0; i--) {
					P[i] += ui;
				}
				u = 0.0;
				break;
			}
			else {
				for (int i = min; i >= 0; i--) {
					P[i] += diff;
					u -= diff;
				}
				min++;
			}
		}
		else {
			min++;
		}
	}
	double prop = 1;
	for (auto p : P) {
		prop *= p;
	};
	return prop;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, K;
		cin >> N >> K;
		double U;
		cin >> U;
		vector<double> P;
		double p;
		for (int i = 0; i < N; i++) {
			cin >> p;
			P.push_back(p);
		}
		cout << "Case #" << t << ": ";
		//cout << N << "->";
		cout.precision(6);
		cout << fixed << solve(N, K, U, P);
		cout << endl;
	}
}

