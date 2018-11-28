#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int n, p;
int r[55];
int q[55][55];

typedef pair<int, int> pii;

#define fst first
#define snd second

pii t[55][555];
int w[55];

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &r[i]);
		}
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j < p; ++ j) {
				scanf("%d", &q[i][j]);
			}
			sort(q[i], q[i] + p);
			for (int j = 0; j < p; ++ j) {
				int lb = int(ceil(q[i][j] / (1.1 * r[i])) + 0.5);
				int rb = int(floor(q[i][j] / (0.9 * r[i])) + 0.5);
				t[i][j] = make_pair(lb, rb);
			}
		}
		int res = 0;

		for (int i = 0; i < n; ++ i) {
			w[i] = 0;
		}

		while (true) {
			bool flag = false;
			for (int i = 0; i < n; ++ i) {
				if (w[i] == p) {
					flag = true;
					break;
				}
			}
			if (flag) {
				break;
			}
			int lb = t[0][w[0]].fst, rb = t[0][w[0]].snd;
			for (int i = 1; i < n; ++ i) {
				lb = max(lb, t[i][w[i]].fst);
				rb = min(rb, t[i][w[i]].snd);
			}
			if (lb <= rb) {
				++ res;
				for (int i = 0; i < n; ++ i) {
					++ w[i];
				}
			} else {
				int who = 0;
				for (int i = 1; i < n; ++ i) {
					if (t[i][w[i]] < t[who][w[who]]) {
						who = i;
					}
				}
				++ w[who];
			}
		}

		printf("Case #%d: %d\n", kase, res);
	}
	return 0;
}
