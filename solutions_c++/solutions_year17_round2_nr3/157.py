#include <iostream>
#include <iomanip>
using namespace std;

long long range[100], speed[100];
long long dists[100][100];
double times[100][100];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, Q;
		cin >> N >> Q;

		for (int i = 0; i < N; i++) {
			cin >> range[i] >> speed[i];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> dists[i][j];
			}
		}

		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (dists[i][k] >= 0 && dists[k][j] >= 0 && (dists[i][j] < 0 || dists[i][j] > dists[i][k]+dists[k][j])) {
						dists[i][j] = dists[i][k]+dists[k][j];
					}
				}
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (dists[i][j] >= 0 && dists[i][j] <= range[i]) {
					times[i][j] = double(dists[i][j])/double(speed[i]);
				} else {
					times[i][j] = -1;
				}
			}
		}

		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (times[i][k] >= -0.5 && times[k][j] >= -0.5 && (times[i][j] < -0.5 || times[i][j] > times[i][k]+times[k][j])) {
						times[i][j] = times[i][k]+times[k][j];
					}
				}
			}
		}

		cout << "Case #" << t << ':';
		for (int q = 0; q < Q; q++) {
			int U, V;
			cin >> U >> V;
			cout << ' ' << setprecision(12) << times[U-1][V-1];
		}
		cout << '\n';
	}

	return 0;
}
