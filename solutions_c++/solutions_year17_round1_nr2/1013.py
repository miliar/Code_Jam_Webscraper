#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

bool IsValid(const pair<int, int> &Range) {
	return Range.first <= Range.second;
}

pair<int, int> Intersection(const pair<int, int> &Lhs, const pair<int, int> &Rhs) {
	return {std::max(Lhs.first, Rhs.first), std::min(Lhs.second, Rhs.second)};
}

pair<int, int> CountRange(int R, int Q) {
	pair<int, int> Range;
	Range.first = int(ceil((Q / double(1.1)) / R));
	Range.second = (Q * 10 / 9) / R;

	return Range;
}

int Solve(int N, int P, const vector<int> &R, vector<vector<int>> &Q) {
	int Kit = 0;

	for (auto &Qi : Q) {
		sort(Qi.begin(), Qi.end());
	}

	while (true) {
		for (auto &Qi : Q) {
			if (Qi.empty()) {
				return Kit;
			}
		}

		pair<int, int> Range = CountRange(R[0], Q[0].back());

		for (int i = 0; i < Q.size(); i++) {
			Range = Intersection(Range, CountRange(R[i], Q[i].back()));
		}

		if (IsValid(Range)) {
			for (auto &Qi : Q) {
				Qi.pop_back();
			}
			if (Range.second > 0) {
				Kit++;
			}
		} else {
			for (int i = 0; i < Q.size(); i++) {
				while (!Q[i].empty()) {
					pair<int, int> IthRange = CountRange(R[i], Q[i].back());
					if (IthRange.first > Range.second) {
						Q[i].pop_back();
					} else {
						break;
					}
				}
			}
		}
	}

	return Kit;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int N, P;
		cin >> N >> P;

		vector<int> R;
		R.resize(N);
		for (int &Ri : R) {
			cin >> Ri;
		}

		vector<vector<int>> Q;
		Q.resize(N);
		for (vector<int> &Qi : Q) {
			Qi.resize(P);
			for (int &Qij : Qi) {
				cin >> Qij;
			}
		}

		cout << "Case #" << i << ": " << Solve(N, P, R, Q) << "\n";
	}
	return 0;
}
