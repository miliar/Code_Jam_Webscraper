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

static int maxIn(const vector<int> &L) {
	for (int i = L.size() - 1; i >= 0; i--) {
		if (L[i] > 0) {
			return i;
		}
	}

	return -1;
}

static int minIn(const vector<int> &L) {
	for (size_t i = 0; i < L.size(); i++) {
		if (L[i] > 0) {
			return i;
		}
	}

	return -1;
}

static void solve() {
	int N, P;
	cin >> N >> P;
	vector<int> L;
	L.resize(P);
	for (int i = 0; i < N; i++) {
		int Gi;
		cin >> Gi;
		L[Gi % P]++;
	}

	if (P == 2) {
		cout << L[0] + (L[1] + 1) / 2;
	} else if (P == 3) {
		int m = min(L[1], L[2]);
		L[1] -= m;
		L[2] -= m;
		int happy = L[0] + m + (L[1] + L[2]) / 3;
		L[1] %= 3;
		L[2] %= 3;
		if (L[1] > 0 || L[2] > 0) {
			happy++;
		}
		cout << happy;
	} else if (P == 4) {
		int m = min(L[1], L[3]);
		L[1] -= m;
		L[3] -= m;
		int happy = L[0] + m + L[2] / 2 + (L[1] + L[3]) / 4;
		int left = 0;
		L[2] %= 2;
		L[1] %= 4;
		L[3] %= 4;
		if (L[1] > 0 || L[2] > 0 || L[3] > 0) {
			happy++;
		}
		cout << happy;
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
