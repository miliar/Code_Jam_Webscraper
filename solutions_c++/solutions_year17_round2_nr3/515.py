#include <cstdio>
#include <iostream>
using namespace std;

long long dist[100][100];
double dtime[100][100];
struct City
{
	int E, S;
};
City cities[100];

bool doit()
{
	int N, Q;
	cin >> N >> Q;
	for (int i = 0; i < N; ++i) {
		cin >> cities[i].E >> cities[i].S;
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> dist[i][j];
		}
	}
	// All pair shortest path in length
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (dist[i][k] == -1)
					continue;
				if (dist[k][j] == -1)
					continue;
				long long totd = dist[i][k] + dist[k][j];
				if (dist[i][j] == -1 || totd < dist[i][j])
					dist[i][j] = totd;
			}
		}
	}
	// Convert to time
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			dtime[i][j] = 100.0*1e9*1e10;  // 1e10 for safety margin
			if (dist[i][j] == -1)
				continue;
			const City &city = cities[i];
			if (dist[i][j] > city.E)
				continue;  // Too far
			dtime[i][j] = (double)dist[i][j] / (double)cities[i].S;
		}
	}
	// All pair shortest path in time
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				double tott = dtime[i][k] + dtime[k][j];
				if (tott < dtime[i][j])
					dtime[i][j] = tott;
			}
		}
	}
	// Calculate each part
	for (int i = 0; i < Q; ++i) {
		int U, V;
		cin >> U >> V;
		printf(" %.6lf", dtime[U-1][V-1]);
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		printf("Case #%d:", t+1);
		doit();
		printf("\n");
	}
	return 0;
}
