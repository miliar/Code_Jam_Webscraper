#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <string.h>
#include <stdlib.h>

#define oo 2000000000

using namespace std;

int n, p, r[55], q[55][55], per[55], bot[55][55], top[55][55], c[3030][3030];
int ar[3030], ord, mark[3030], f[3030][3030], pre[3030];
vector<int> nxt[3030];

bool findpath () {
    ar[1] = 0; ++ord;
    int l = 1, r = 1;
    while (l <= r) {
        int u = ar[l];
        int s = nxt[u]. size ();
        for(int i = 0; i <= s - 1; i++) {
            int v = nxt[u][i];
            if (mark[v] == ord) continue;
            if (f[u][v] >= c[u][v]) continue;
            mark[v] = ord; pre[v] = u;
            if (v == n * p + 1) return true;
            ar[++r] = v;
        }
        ++l;
    }
    return false;
}
 
void incflow () {
    int v = n * p + 1;
    int k = oo;
    while (v != 0) {
        int u = pre[v];
        k = min (k, c[u][v] - f[u][v]);
        v = u;
    }
    v = n * p + 1;
    while (v != 0) {
        int u = pre[v];
        f[u][v] += k;
        f[v][u] -= k;
        v = u;
    }
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("rat.out", "w", stdout);
	int test; scanf("%d", &test);
	for(int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		scanf("%d%d", &n, &p);
		ord = 0;
		for(int i = 0; i <= n * p + 1; i++) {
			for(int j = 0; j <= n * p + 1; j++) c[i][j] = f[i][j] = 0;
			nxt[i].clear();
			mark[i] = 0;
			pre[i] = 0;
		}
		for(int i = 1; i <= n; i++) scanf("%d", &r[i]);
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= p; j++) {
				scanf("%d", &q[i][j]);
				bot[i][j] = (int)ceil((q[i][j] / 1.1) / r[i]);
				top[i][j] = (int)floor((q[i][j] / 0.9) / r[i]);
				if (bot[i][j] > top[i][j]) continue;
				if (i > 1) {
					int x = (i - 1) * p + j;
					for(int k = 1; k <= p; k++) {
						if (!(top[i - 1][k] < bot[i][j] || top[i][j] < bot[i - 1][k])) {
							c[(i - 2) * p + k][x] = 1;
							nxt[(i - 2) * p + k].push_back(x);
							nxt[x].push_back((i - 2) * p + k);
						}
					}
				}
				else {
					c[0][j] = 1;
					nxt[0].push_back(j);
					nxt[j].push_back(0);
				}
			}
		}
		for(int i = 1; i <= p; i++) {
			if (bot[n][i] > top[n][i]) continue;
			c[(n - 1) * p + i][n * p + 1] = 1;
			nxt[(n - 1) * p + i].push_back(n * p + 1);
			nxt[n * p + 1].push_back((n - 1) * p + i);
		}
		while (1) {
			if (findpath()) incflow();
			else break;
		}
		int res = 0, ss = nxt[0].size();
		for(int i = 0; i < ss; i++) res += f[0][nxt[0][i]];
		printf("%d\n", res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}