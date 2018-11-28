#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

bool isImpossible(vector<int>& v) {
	for (int i = 1; i < 6; i += 2) {
		if (v[i] > v[(i+3)%6]) {
			return 1;
		}
	}
	return 0;
}

vector<char> letter = {'R', 'O', 'Y', 'G', 'B', 'V'};

void solve(int test) {
	cout << "Case #" << test << ": ";
	int sum;
	cin >> sum;
	vector<int> v(6);
	vector<bool> done(6);
	for (int i = 0; i < 6; ++i) {
		cin >> v[i];
	}

	for (int i = 0; i < 6; i += 2) {
		if (v[i] == v[(i+3) % 6] && v[i] + v[(i+3) % 6] == sum) {
			for (int cnt = 1; cnt <= v[i]; ++cnt) {
				cout << letter[i] << letter[(i+3)%6];
			}
			cout << "\n";
			return;
		}
	}

	string sol;

	if (isImpossible(v)) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	// cerr << "Here\n";

	sum = 0;
	for (int i = 0; i < 6; i += 2) {
		v[i] -= v[(i+3) % 6];
		sum += v[i];
	}

	int last = -1, initial = -1;

	// cerr << sum << "\n";

	for (int i = 1; i <= sum; ++i) {
		int maxj = -1;
		for (int j = 0; j < 6; j += 2) {
			if (j != last) {
				if(j == -1 || v[maxj] < v[j] || (v[maxj] == v[j] && j == initial)) {
					maxj = j;
				}
			}
		}

		if (i == 1) {
			initial = maxj;
		}

		if (v[maxj] == 0 || (i == sum && maxj == initial)) {
			cout << "IMPOSSIBLE\n";
			return;
		}

		if (done[maxj]) {
			sol += letter[maxj];
		} else {
			sol += letter[maxj];
			for (int cnt = 1; cnt <= v[(maxj+3)%6]; ++cnt) {
				sol += letter[(maxj+3)%6];
				sol += letter[maxj];
			}
			done[maxj] = true;
		}

		v[maxj]--;
		last = maxj;
	}

	cout << sol << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}