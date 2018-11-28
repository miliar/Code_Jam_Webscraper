#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <cstdio>

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;


lld d[111][111];
int n, q, dist[111], spd[111];
double d2[111][111];

void solve_case() {
	cin >> n >> q;
	for (int i=1; i<=n; i++) {
		cin >> dist[i] >> spd[i];
	}
	for (int i=1; i<=n; i++) {
		for (int j=1; j<=n; j++) {
			cin >> d[i][j];
			if (d[i][j] == -1) {
				d[i][j] = 1000000000LL * 1000000LL;
			}
		}
	}

	for (int k=1; k<=n; k++) {
		for (int i=1; i<=n; i++) {
			for (int j=1; j<=n; j++) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
	for (int i=1; i<=n; i++) {
		for (int j=1; j<=n; j++) {
			if (d[i][j] <= dist[i]) {
				d2[i][j] = double(d[i][j]) / double(spd[i]);
			} else {
				d2[i][j] = 1000000000000000.;
			}
		}
	}
	
	for (int k=1; k<=n; k++) {
		for (int i=1; i<=n; i++) {
			for (int j=1; j<=n; j++) {
				d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);
			}
		}
	}
	
	while (q--) {
		int st, me;
		cin >> st >> me;
		printf("%.6f ", d2[st][me]);
	}
	printf("\n");
}


int main () {
    int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}
