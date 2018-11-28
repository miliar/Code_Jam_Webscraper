#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <list>
#include <array>
#include <map>
#include <algorithm>
#include <set>
#include <utility>
#include <cmath>
using namespace std;

static void solveSmall() {
	int N, C, M;
	cin >> N >> C >> M;
	int T[2][1000] = {};
	for (int i = 0; i < M; i++) {
		int Pi, Bi;
		cin >> Pi >> Bi;
		T[Bi - 1][Pi - 1]++;
	}

	int Run = 0, Promo = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; T[0][i] > 0 && j < N; j++) {
			if (i == j) {
				continue;
			}
			if (T[0][j] > 0 && T[1][j] > 0) {
				int r = min(T[0][i], T[1][j]);
				T[0][i] -= r;
				T[1][j] -= r;
				Run += r;
			}
		}
		for (int j = 0; T[0][i] > 0 && j < N; j++) {
			if (i == j) {
				continue;
			}
			if (T[1][j] > 0) {
				int r = min(T[0][i], T[1][j]);
				T[0][i] -= r;
				T[1][j] -= r;
				Run += r;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; T[1][i] > 0 && j < N; j++) {
			if (i == j) {
				continue;
			}
			if (T[0][j] > 0 && T[1][j] > 0) {
				int r = min(T[1][i], T[0][j]);
				T[1][i] -= r;
				T[0][j] -= r;
				Run += r;
			}
		}
		for (int j = 0; T[1][i] > 0 && j < N; j++) {
			if (i == j) {
				continue;
			}
			if (T[0][j] > 0) {
				int r = min(T[1][i], T[0][j]);
				T[1][i] -= r;
				T[0][j] -= r;
				Run += r;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		if (T[0][i] > 0 || T[1][i] > 0) {
			if (i == 0) {
				int r = T[0][i] + T[1][i];
				Run += r;
			} else {
				int r = max(T[0][i], T[1][i]);
				Promo = min(T[0][i], T[1][i]);
				Run += r;
			}
		}
	}

	cout << Run << " " << Promo;
}

static void solve() {
	solveSmall();
	return;


	int N, C, M;
	cin >> N >> C >> M;
	vector<pair<int, int>> PB;
	for (int i = 0; i < C; i++) {
		int Pi, Bi;
		cin >> Pi >> Bi;
		PB.emplace_back(Pi, Bi);
	}

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
