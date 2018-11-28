#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;

int n;
double best[111][111];
int dist[111][111];
int e[111], s[111];
bool vis[111];


void pre () {
	for (int r=0;r<n;r++) {
		memset (vis, 0, sizeof(vis));
		int nxt = r, c;
		while (nxt != -1) {
			c = nxt;
			vis[c] = true;
			double l = (double)(e[r]) - best[r][c]*s[r];
			for (int i=0;i<n;i++) {
				if (dist[c][i] != -1 && (l - (double)dist[c][i] >= -1e-9)) {
					if (best[r][i] > best[r][c] + ((double)(dist[c][i]) / (double)(s[r]))) {
						best[r][i] = best[r][c] + ((double)(dist[c][i]) / (double)(s[r]));
					}
				}
			}
			double b = 1e14;
			nxt = -1;
			for (int i=0;i<n;i++) {
				if (vis[i]) {
					continue;
				}
				if (b - best[r][i] > 1e-9) {
					b = best[r][i];
					nxt = i;
				}
			}
		}
	}
}

void floyd () {
	for (int k=0;k<n;k++) {
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				best[i][j] = min (best[i][j], best[i][k]+best[k][j]);
			}
		}
	}
}

void dump () {
	for (int i=0;i<n;i++) {
		for (int j=0;j<n;j++) {
			printf ("%.9lf ", best[i][j]);
		}
		printf ("\n");
	}
}

int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		int q;	
		scanf ("%d %d", &n, &q);
		for (int i=0;i<n;i++) {
			scanf ("%d %d", &e[i], &s[i]);
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				best[i][j] = 1e14;
				scanf ("%d", &dist[i][j]);
			}
			best[i][i] = 0;
		}

		pre ();
		//dump();
		floyd ();
		//dump();

		printf ("Case #%d: ", tc);
		for (int i=0;i<q;i++) {
			int u, v;
			scanf ("%d %d", &u, &v);
			u --, v--;
			printf (" %.9lf", best[u][v]);
		}
		printf ("\n");
	}

	return 0;
}