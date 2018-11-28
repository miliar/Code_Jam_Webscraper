#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

using big = long long;

using namespace std;

const int N = 203;

long long dis[N][N];
double t[N][N];
const big inf = 1ll << 60;
const double infd = 2e12;

struct Q {
	int from, to;
} q[N];
int n, m;
struct H {
	int dis;
	double spd;
} horse[N];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);

	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d:", cass);
		cerr << "case " << cass << endl;
		cin >> n >> m;

		for (int i = 1; i <= n; ++i) {
			cin >> horse[i].dis >> horse[i].spd;
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				cin >> dis[i][j];
				if (dis[i][j] == -1) {
					dis[i][j] = inf;
				}
			}
		}
		for (int i = 1; i <= m; ++i) {
			cin >> q[i].from >> q[i].to;
		}
		for (int k = 1; k <= n; ++k) {
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= n; ++j) {
					dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
				}
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (i == j) {
					t[i][j] = 0;
					continue;
				}
				if (horse[i].dis >= dis[i][j]) {
					t[i][j] = dis[i][j] / horse[i].spd;
				} else {
					t[i][j] = infd;
				}
			}
		}
//		cerr << "dis: " << endl;
//		for (int i = 1; i <= n; ++i, cerr << endl) {
//			for (int j = 1; j <= n; ++j) {
//				cerr << dis[i][j] << " ";
//			}
//		}
//		cerr << "T: " << endl;
//		for (int i = 1; i <= n; ++i, cerr << endl) {
//			for (int j = 1; j <= n; ++j) {
//				cerr << t[i][j] << " ";
//			}
//		}
		for (int k = 1; k <= n; ++k) {
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= n; ++j) {
					double newt = t[i][k] + t[k][j];
					t[i][j] = min(t[i][j], newt);
				}
			}
		}
		for (int i = 1; i <= m; ++i) {
			printf(" %.6f", t[q[i].from][q[i].to]);
		}
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
}

