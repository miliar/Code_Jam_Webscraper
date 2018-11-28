#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, P;

bool done(const vector<int> &I) {
	for (int i = 0; i < N; i++) {
		if (I[i] == P) return true;
	}
	return false;
}

pair<int, int> inter(pair<int, int> a, pair<int, int> b) {
	int from = max(a.first, b.first),
		to = min(a.second, b.second);

	if (from > to) {
		return { -1, -1 };
	}

	return { from, to };
}

struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.second < right.second;
    }
};

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N >> P;

		int ans = 0;
		vector<int> R(N), I(N);
		vector<vector<pair<int, int> > > Q(N, vector<pair<int, int> >(P));

		for (int i = 0; i < N; i++) {
			cin >> R[i];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				int v;
				cin >> v;

				int lb = (10 * v) / (11 * R[i]) + ((10 * v) % (11 * R[i]) > 0),
					ub = (10 * v) / (9 * R[i]);

				//cout << "LBUB " << lb << " " << ub << endl;

				if (lb > ub) {
					Q[i][j] = { -1, -1 };
				} else Q[i][j] = { lb, ub };
			}
			sort(Q[i].begin(), Q[i].end(), sort_pred());
		}

		while (!done(I)) {
			pair<int, int> itv = { 1, 1 << 30 };
			for (int i = 0; i < N; i++) {
				// cout << itv.first << " " << itv.second << " "
				// 	 << Q[i][I[i]].first << " " << Q[i][I[i]].second << endl;
				itv = inter(itv, Q[i][I[i]]);
				if (itv.first == -1 && itv.second == -1) {
					break;
				}
			}
			if (itv.first != -1 && itv.second != -1) {
				//cout << itv.first << " " << itv.second << endl;
				ans++;
				for (int i = 0; i < N; i++) I[i]++;
			} else {
				int sm = 1 << 30, j = -1;
				for (int i = 0; i < N; i++) {
					if (Q[i][I[i]].second < sm) {
						sm = Q[i][I[i]].second;
						j = i;
					}
				}
				I[j]++;
			}
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}