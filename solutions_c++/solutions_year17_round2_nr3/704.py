#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <cstdlib>
#include <memory.h>
#include <ctime>
#include <bitset>

using namespace std;

#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.1415926535897
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned

int e[110];
int s[110];
LL d[110][110];
int u[110];
int v[110];
int n, q;
LL INF = 1000000000000000000ll;
double dist[110];
int was[110];

set<pair<double, int>> se;

int main()
{
#ifdef Fcdkbear
	freopen("in.txt", "r", stdin);
	double beg = clock();
	freopen("out.txt", "w", stdout);
#endif

	int tests;
	scanf("%d", &tests);
	FOR(testNumber, 1, tests + 1) {
		cin >> n >> q;
		FOR(i, 0, n) {
			cin >> e[i] >> s[i];
		}
		FOR(i, 0, n) {
			FOR(j, 0, n) {
				cin >> d[i][j];
			}
		}
		FOR(i, 0, n) {
			d[i][i] = 0;
		}
		FOR(i, 0, n) {
			FOR(j, 0, n) {
				if (d[i][j] == -1) {
					d[i][j] = INF;
				}
			}
		}
		FOR(k, 0, n) {
			FOR(i, 0, n) {
				FOR(j, 0, n) {
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}
		double res = 1e40;
		FOR(i, 0, q) {
			cin >> u[i] >> v[i];
			u[i]--;
			v[i]--;
		}
		printf("Case #%d:", testNumber);
		FOR(it, 0, q) {
			FOR(i, 0, n) {
				dist[i] = 1e40;
			}
			dist[u[it]] = 0;
			MEMS(was, 0);
			se.clear();
			se.insert(mp(0, u[it]));
			while (se.size()) {
				int v = se.begin()->second;
				se.erase(se.begin());
				if (was[v]) {
					continue;
				}
				was[v] = 1;
				FOR(i, 0, n) {
					if (e[v] >= d[v][i]) {
						double ti = d[v][i] / (double)s[v];
						if (dist[v] + ti < dist[i]) {
							se.erase(mp(dist[i], i));
							dist[i] = dist[v] + ti;
							se.insert(mp(dist[i], i));
						}
					}
				}
			}
			printf(" %.15lf", dist[v[it]]);
		}
		printf("\n");
	}

#ifdef Fcdkbear
	double end = clock();
	fprintf(stderr, "*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
#endif
	return 0;
}