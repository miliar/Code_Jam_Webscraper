#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cout << "Case #" << test << ": ";
		int N, Q;
		cin >> N >> Q;
		vector<double> E(N), S(N);
		for (int i = 0; i < N; ++i) {
			cin >> E[i] >> S[i];
		}
		vector<vector<double> > D(N, vector<double> (N));
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				cin >> D[i][j];
			}
		}
		assert(Q == 1);
		int s, t;
		cin >> s >> t;
		vector<vector<double> > w(N, vector<double> (N, -1));
		for (int i = 0; i < N; ++i) {
			double d_traveled = 0;
			for (int j = i + 1; j < N; ++j) {
				d_traveled += D[j - 1][j];
				if (d_traveled > E[i]) {
					break;
				} else {
					double tmp = d_traveled / S[i];
					if (w[i][j] < 0 || w[i][j] > tmp) {
						w[i][j] = tmp;
					}
				}
			}
		}
		vector<double> dist(N, -1);
		dist[0] = 0;
		for (int i = 1; i < N; ++i) {
			for (int j = 0; j < i; ++j) {
				if (w[j][i] >= 0) {
					double tmp = dist[j] + w[j][i];
					if (dist[i] < 0 || dist[i] > tmp) {
						dist[i] = tmp;
					}
				}
			}
		}
		printf("%.6lf\n", dist[N-1]);
	}
	return 0;
}

