#include <bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define emp emplace
#define fi first
#define se second
#define INF 0x3f3f3f3f
typedef long long ll;
typedef pair<int,int> ii;

int n, m;
char g[30][30];

bool allClear(int x) {
	for (int i = 0; i < m; i++) {
		if (g[x][i] != '?') return false;
	}

	return true;
}

int main(void) {
	ios_base::sync_with_stdio(false);

	int t;cin >> t;

	int cnt = 1;
	while (t--) {
		cin >> n >> m;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> g[i][j];
			}
		}

		for (int i = 0; i < n; i++) {
			if (allClear(i) and i) {
				for (int j = 0; j < m; j++) g[i][j] = g[i-1][j];
			} else {
				for (int j = 0; j < m; j++) {
					if (g[i][j] == '?') continue;
					int aux = j;

					j++;
					while (j < m and g[i][j] == '?') {
						g[i][j] = g[i][aux];
						j++;
					}
					j--;
				}
				for (int j = m-1; j >= 0; j--) {
					if (g[i][j] == '?') continue;
					int aux = j;

					j--;
					while (j >= 0 and g[i][j] == '?') {
						g[i][j] = g[i][aux];
						j--;
					}
					j++;
				}
			}
		}
		for (int i = n-2; i >= 0; i--) {
			if (allClear(i)) {
				for (int j = 0; j < m; j++) g[i][j] = g[i+1][j];
			}
		}

		cout << "Case #" << cnt++ << ":" << endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << g[i][j];
			}
			cout << endl;
		}
	}
    
	return 0;
}

