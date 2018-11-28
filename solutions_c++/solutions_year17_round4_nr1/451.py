#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, p, n, c[5], y[5];
short dp[101][101], dp3[101][101][101], dp4[101][101][101][101];

short max(short x, short y) {
	return (x < y) ? y : x;
}

void doit(int abc) {
	cout << "Case #" << abc+1 << ": ";
	cin >> n >> p;
	memset(c, 0, sizeof(c));

	for (int i = 0; i < n; ++i) {
		int x; cin >> x;
		c[x%p]++;
	}

	if (p == 2) {
		memset(dp, 0, sizeof(dp));

		for (y[0] = 0; y[0] <= c[0]; ++y[0])
			for (y[1] = 0; y[1] <= c[1]; ++y[1]) {
				if (y[0] == 0 && y[1] == 0) {
					continue;
				}

				int s = 0;
				for (int i = 0; i < p; ++i)
					s += i*(c[i] - y[i]);
				int add = ((s%p) == 0);
				if (y[0] > 0)
					dp[y[0]][y[1]] = max(dp[y[0]][y[1]], dp[y[0]-1][y[1]]+add);
				if (y[1] > 0)
					dp[y[0]][y[1]] = max(dp[y[0]][y[1]], dp[y[0]][y[1]-1]+add);
			}

		cout << dp[c[0]][c[1]] << endl;
	}
	
	if (p == 3) {
		memset(dp3, 0, sizeof(dp3));

		for (y[0] = 0; y[0] <= c[0]; ++y[0])
			for (y[1] = 0; y[1] <= c[1]; ++y[1])
				for (y[2] = 0; y[2] <= c[2]; ++y[2]) {
					if (y[0] == 0 && y[1] == 0 && y[2] == 0) {
						continue;
					}

					int s = 0;
					for (int i = 0; i < p; ++i)
						s += i*(c[i] - y[i]);
					int add = ((s%p) == 0);

					if (y[0] > 0)
						dp3[y[0]][y[1]][y[2]] = max(dp3[y[0]][y[1]][y[2]], dp3[y[0]-1][y[1]][y[2]]+add);
					if (y[1] > 0)
						dp3[y[0]][y[1]][y[2]] = max(dp3[y[0]][y[1]][y[2]], dp3[y[0]][y[1]-1][y[2]]+add);
					if (y[2] > 0)
						dp3[y[0]][y[1]][y[2]] = max(dp3[y[0]][y[1]][y[2]], dp3[y[0]][y[1]][y[2]-1]+add);
				}

		cout << dp3[c[0]][c[1]][c[2]] << endl;
	}

	if (p == 4) {
		memset(dp4, 0, sizeof(dp4));

		for (y[0] = 0; y[0] <= c[0]; ++y[0])
			for (y[1] = 0; y[1] <= c[1]; ++y[1])
				for (y[2] = 0; y[2] <= c[2]; ++y[2])
					for (y[3] = 0; y[3] <= c[3]; ++y[3]) {
						if (y[0] == 0 && y[1] == 0 && y[2] == 0 && y[3] == 0) {
							continue;
						}

						int s = 0;
						for (int i = 0; i < p; ++i)
							s += i*(c[i] - y[i]);
						int add = ((s%p) == 0);

						if (y[0] > 0)
							dp4[y[0]][y[1]][y[2]][y[3]] = max(dp4[y[0]][y[1]][y[2]][y[3]], dp4[y[0]-1][y[1]][y[2]][y[3]]+add);
						if (y[1] > 0)
							dp4[y[0]][y[1]][y[2]][y[3]] = max(dp4[y[0]][y[1]][y[2]][y[3]], dp4[y[0]][y[1]-1][y[2]][y[3]]+add);
						if (y[2] > 0)
							dp4[y[0]][y[1]][y[2]][y[3]] = max(dp4[y[0]][y[1]][y[2]][y[3]], dp4[y[0]][y[1]][y[2]-1][y[3]]+add);
						if (y[3] > 0)
							dp4[y[0]][y[1]][y[2]][y[3]] = max(dp4[y[0]][y[1]][y[2]][y[3]], dp4[y[0]][y[1]][y[2]][y[3]-1]+add);

					}

		cout << dp4[c[0]][c[1]][c[2]][c[3]] << endl;
	}
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		doit(i);	
}