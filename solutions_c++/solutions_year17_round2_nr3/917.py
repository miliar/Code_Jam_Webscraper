#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <limits.h>
#include <math.h>
#include <unordered_map>
#include <assert.h>
using namespace std;

#define ran(i, a, b) for ((i) = (a); (i) < (b); (i)++)
#define rep(i, a) ran ((i), 0, (a))
#define rep1(i, a) ran ((i), 1, (a)+1)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
#define _0 first
#define _1 second
#define _pb(x) push_back(x)
#define _mp(x, y) make_pair(x, y)
#if defined(SHIROKO1_LOCAL) && !defined(NDEBUG)
#define DEBUG(...) fprintf(stderr, "[DEBUG] " __VA_ARGS__)
#else
#define DEBUG(...) ((void)0)
#endif

static const double INF = HUGE_VAL;

struct solve {

	int N;
	double D[100][100];
	double dist[100][100];
	double time[100][100];
	int seen[100][100];
	int gid;
	struct horse {
		int e, s;
	} H[100];

	solve() {
		int q;
		cin >> N;
		cin >> q;
		int i;
		rep (i, N)
			cin >> H[i].e >> H[i].s;
		int j;
		rep (i, N)
		rep (j, N) {
			cin >> D[i][j];
			if (D[i][j] < 0)
				D[i][j] = INF;
		}
		calc();
		rep (i, q) {
			int u, v;
			cin >> u >> v;
			printf(" %.13lf", answer(u, v));
		}
		putchar('\n');
	}

#ifndef NDEBUG
	template <typename T>
	void dump(T x[100][100])
	{
		int i, j;
		rep (i, N) {
			rep (j, N-1) {
				cerr << x[i][j] << ' ';
			}
			cerr << x[i][j] << '\n';
		}
	}
#else
#define dump(x)
#endif

	void calc() {
		int i, j, k;
		rep (i, N)
		rep (j, N)
			dist[i][j] = D[i][j];
		rep (i, N)
			dist[i][i] = 0;
		DEBUG("given dist\n");
		dump(dist);
		rep (k, N)
		rep (i, N)
		rep (j, N) {
			auto t = dist[i][k] + dist[k][j];
			dist[i][j] = min(dist[i][j], t);
		}
		DEBUG("real dist\n");
		dump(dist);
		rep (i, N)
		rep (j, N) {
			if (dist[i][j] <= H[i].e)
				time[i][j] = dist[i][j] / H[i].s;
			else
				time[i][j] = INF;
		}
		DEBUG("times\n");
		dump(time);
		rep (k, N)
		rep (i, N)
		rep (j, N) {
			auto t = time[i][k] + time[k][j];
			time[i][j] = min(time[i][j], t);
		}
		DEBUG("final times\n");
		dump(time);
	}

	double answer(int s, int d) {
		return time[s-1][d-1];
	}

};

int main()
{
	int t, i;
	cin >> t;
	rep1 (i, t) {
		printf("Case #%i:", i);
		solve();
	}
	return 0;
}
