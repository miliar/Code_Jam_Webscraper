#include <bits/stdc++.h>

using namespace std;

int dp[100][100];
int q[100][100];
int mx[100][100], mi[100][100];
int low[100][100], high[100][100];
int n, p;
int need[100];
int pos[100];


int main() {

	int T;
	cin >> T;
	for (int ka = 1; ka <= T; ka++) {
		cin >> n >> p;

		for (int i = 0; i < n; i++) 
			cin >> need[i];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				cin >> q[i][j];
			}
			sort(q[i], q[i] + p);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				low[i][j] = (int)ceil(q[i][j]/(need[i]*1.1));
				high[i][j] = (int)(q[i][j]/(need[i] * 0.9));
				//printf("(%d, %d) ", low[i][j], high[i][j]);
			}
			//printf("\n");
		}

		int ans = 0;

		memset(pos, 0, sizeof(pos));

		bool ok = true;

		while(ok) {
			int l = -1, r = 10000000;
			for (int i = 0; i < n; i++) {
				l = max(l, low[i][pos[i]]);
				r = min(r, high[i][pos[i]]);
			}
			if (l <= r) {
				ans++;
				for (int i = 0; i < n; i++) {
					pos[i]++;
					if (pos[i] >= p) ok = 0;
				}
			}
			else {
				int minid = 0, minr = high[0][pos[0]];
				for (int i = 1; i < n; i++) {
					if (high[i][pos[i]] < minr) {
						minid = i;
						minr = high[i][pos[i]];
					}
				}
				pos[minid]++;
				if (pos[minid] >= p) ok = 0;
			}
		}

		printf("Case #%d: %d\n", ka, ans);
	}

	return 0;
}