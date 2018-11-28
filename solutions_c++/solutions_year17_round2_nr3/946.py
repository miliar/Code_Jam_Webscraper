#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const double inf = 10e+10;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

const double eps = 10e-7;

bool eq(const double &a, const double &b) {
	return fabs(a - b) < eps;
}

void clear(int i) {

}

const int size = 101;


int solution(int nTest) {
	int n, q;
	scanf("%d%d", &n, &q);
	vector<pair<double, double> > horse;
	For (i, 0, n) {
		int e, s;
		scanf("%d%d", &e, &s);
		horse.pb(mp((double)e, (double)s));
	}
	vector<vector<lint> > G(n, vector<lint>(n));
	For (i, 0, n) {
		For (j, 0, n) {
			scanf("%lld", &G[i][j]);
		}
	}
	For (i, 0, n) {
		G[i][i] = 0;
	}
	For (k, 0, n) {
		For (i, 0, n) {
			For (j, 0, n) {
				if (G[i][k] == -1 || G[k][j] == -1) {
					continue;
				}
				lint nd = G[i][k] + G[k][j];
				if (G[i][j] == -1) {
					G[i][j] = nd;
				} else {
					G[i][j] = min(G[i][j], nd);
				}
			}
		}
	}
	//if (nTest == 80) { For (i, 0, n) { For(j, 0, n) cerr << G[i][j] << " "; cerr << endl;} }

	/*
	vector<vector<vector<pair<double, double> > > > dp(n, vector<vector<pair<double, double> > >(n, vector<pair<double, double> >(n, mp(inf, 0))));
	For (i, 0, n) {
		dp[i][i][i] = mp(0., horse[i].first);
	}
	For (i, 0, n) {
		For (j, 0, n) {
			if (G[i][j] == -1) {
				continue;
			}
			double d = G[i][j];
		}
	}
	For (k, 0, n) {
		For (u, 0, n) {
			For (v, 0, n) {
			}
		}
	}
	*/

	vector<vector<double> > dp(n, vector<double>(n, inf));
	For (i, 0, n) {
		dp[i][i] = 0;
	}
	For (i, 0, n) {
		For (j, 0, n) {
			if (G[i][j] == -1) {
				continue;
			}
			double d = G[i][j];
			double e = horse[i].first;
			double s = horse[i].second;
			if (d < e || eq(d, e)) {
				dp[i][j] = d / s;
			}
		}
	}
	For (k, 0, n) {
		For (i, 0, n) {
			For (j, 0, n) {
				if (eq(dp[i][k], inf) || eq(dp[k][j], inf)) {
					continue;
				}
				dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
			}
		}
	}
	For (i, 0, q) {
		int u, v;
		scanf("%d%d", &u, &v);
		u--;
		v--;
		printf("%.8lf", dp[u][v]);
		if (i < q - 1) {
			printf(" ");
		}
	}
	printf("\n");


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
