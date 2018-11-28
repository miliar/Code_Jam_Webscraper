#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <string>
using namespace std;

double _Solve(const vector<int> &E, const vector<int> &S, const vector<vector<int>> &D, const pair<int, int> &UV) {
	vector<double> TimeToV;

	for (int i = 0; i < E.size(); i++) {
		TimeToV.push_back(-1.0);
	}
	TimeToV.back() = 0;

	for (int i = E.size() - 2; i >= 0; i--) {
		int Distance = 0;
		for (int j = i + 1; j < E.size(); j++) {
			Distance += D[j-1][j];

			if (Distance > E[i]) {
				break;
			}

			double TimeIToJWithIHorse = static_cast<double>(Distance) / S[i];

			if (TimeToV[i] < 0) {
				TimeToV[i] = TimeIToJWithIHorse + TimeToV[j];
			} else {
				TimeToV[i] = std::min(TimeToV[i], TimeIToJWithIHorse + TimeToV[j]);
			}
		}
	}

	return TimeToV[0];
}

vector<double> Solve(const vector<int> &E, const vector<int> &S, const vector<vector<int>> &D, const vector<pair<int, int>> &UV) {
	vector<double> answer;

	for (auto &uv : UV) {
		answer.push_back(_Solve(E, S, D, uv));
	}

	return answer;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int N, Q;
		cin >> N >> Q;

		vector<int> E;
		vector<int> S;

		for (int j = 0; j < N; j++) {
			int Ei, Si;
			cin >> Ei >> Si;
			E.push_back(Ei);
			S.push_back(Si);
		}

		vector<vector<int>> D;
		D.resize(N);
		for (int j = 0; j < N; j++) {
			D[j].resize(N);
			for (int k = 0; k < N; k++) {
				cin >> D[j][k];
			}
		}

		vector<pair<int, int>> UV;

		for (int j = 0; j < Q; j++) {
			int Uj, Vj;
			cin >> Uj >> Vj;
			Uj--;
			Vj--;
			UV.emplace_back(Uj, Vj);
		}

		cout << "Case #" << i << ":";
		auto Ans = Solve(E, S, D, UV);
		for (double value : Ans) {
			printf(" %.7lf", value);
		}
		cout << "\n";
	}
	return 0;
}
