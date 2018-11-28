#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <algorithm>
#include <ctime>
using namespace std;

int const MAX_N = 128;
int const MAX_CH = 5000010;
int const INT_INF = 1000000000;
long long const LL_INF = 1000000000000000000LL;

char st[MAX_CH];

struct pony {
	long long dst, speed;
} HH[MAX_N];

long long sm[MAX_N][MAX_N], min_dist[MAX_N][MAX_N];
double dst[MAX_N];
int nnew[MAX_N];

double const EPS = 1e-8;

double travel_by(int v, pony T, int to, int n) {
	if (min_dist[v][to] > LL_INF/2)
		return 1e100;
	if (min_dist[v][to] > T.dst)
		return 1e100;
	return min_dist[v][to] / ((double) T.speed);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
		int n,q;
		scanf("%d%d",&n,&q);
		for (int i=0; i<n; i++) scanf("%lld%lld",&HH[i].dst,&HH[i].speed);
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				scanf("%lld",&sm[i][j]);

		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++) {
				min_dist[i][j] = sm[i][j];
				if (min_dist[i][j] < 0)
					min_dist[i][j] = LL_INF;
			}

		for (int k=0; k<n; k++)
			for (int i=0; i<n; i++)
				for (int j=0; j<n; j++)
					min_dist[i][j]=min(min_dist[i][j],min_dist[i][k]+min_dist[k][j]);

		printf("Case #%d:",qq+1);

		for (int ee=0; ee<q; ee++) {
			int x,y;
			scanf("%d%d",&x,&y);
			x--; y--;

			for (int i=0; i<n; i++) dst[i] = 1e100;
			dst[x] = 0.0;
			for (int i=0; i<n; i++) nnew[i] = 0;

			while (1) {
				double mn = 1e100;
				int v = -1;
				for (int i=0; i<n; i++)
					if (dst[i] < mn - EPS && !nnew[i]) {
						mn = dst[i];
						v = i;
					}
				if (v < 0) break;

				nnew[v] = 1;
				for (int i=0; i<n; i++)
					if (!nnew[i]) {
						double new_tm = travel_by(v, HH[v], i, n);
						new_tm += dst[v];

						if (dst[i] > new_tm + EPS)
							dst[i] = new_tm;
					}
			}

			printf(" %.15lf",dst[y]);
		}
		printf("\n");
	}
	
	return 0;
}