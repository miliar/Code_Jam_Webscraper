#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

void solve(int test) {
	int N, Q;
	cin >> N >> Q;
	vector<pair<long long, long long> > maxd(N);
	for (int i = 0; i < N; ++i) {
		cin >> maxd[i].first >> maxd[i].second;
	}
	vector<vector<long long> > curdist(N);
	vector<vector<double> > curtime(N);
	for (int i = 0; i < N; ++i) {
		curdist[i].resize(N);
		curtime[i].resize(N);
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> curdist[i][j];
			if (curdist[i][j] < 0)
				curdist[i][j] = 1e18;
			curtime[i][j] = 1e18;
		}
	}
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				curdist[i][j] = min(curdist[i][j], curdist[i][k] + curdist[k][j]);
			}
		}
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (curdist[i][j] <= maxd[i].first) {
				curtime[i][j] = min(curtime[i][j], curdist[i][j] * 1.0 / maxd[i].second);
			}
		}
	}
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				curtime[i][j] = min(curtime[i][j], curtime[i][k] + curtime[k][j]);
			}
		}
	}
	printf("Case #%d: ", test);
	for (int i = 0; i < Q; ++i) {
		int a, b;
		cin >> a >> b;
		a--, b--;
		printf("%.10lf ", curtime[a][b]);
	}
	cout << endl;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}