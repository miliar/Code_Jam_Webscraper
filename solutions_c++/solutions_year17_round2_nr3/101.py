#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define FO(i, a, b) for (int i=(a); i<(b); i++)
#define FOR(i, n) FO(i, 0, n)
#define MAXN 110

int n, q;
double M[MAXN][MAXN];
double T[MAXN][MAXN];
const double inf = 1e25;

vector <double> dijkstra(int start, double F[MAXN][MAXN]){
	vector <double> mdist(n, inf);
	mdist[start] = 0;
	vector <bool> closed(n, false);

	while (true){
		int v = -1;
		FOR(i, n)
			if (!closed[i] && (v == -1 || mdist[i] <= mdist[v]))
				v = i;

		if (v == -1)
			break;

		closed[v] = true;

		FOR(s, n)
			mdist[s] = min(mdist[s], mdist[v] + F[v][s]);
	}

	return mdist;
}


void solve(void)
{
	cin >> n >> q;
	vector <int> e(n), sp(n);
	FOR(i, n)
		cin >> e[i] >> sp[i];

	FOR(i, n){
		FOR(j, n){
			cin >> M[i][j];
			if (M[i][j] == -1)
				M[i][j] = inf;
		}
	}

	FOR(start, n){
		vector <double> mdist = dijkstra(start, M);
		FOR(s, n)
			T[start][s] = (mdist[s] <= e[start]) ? mdist[s] / sp[start] : inf;
	}

	/*cout << '\n';
	FOR(i, n){
		FOR(j, n)
			cout << T[i][j] << ' ';
		cout << '\n';
	}
	cout << '\n';*/

	FOR(qu, q){
		int start, end;
		cin >> start >> end;
		start--, end--;
		vector <double> mdist = dijkstra(start, T);
		cout << fixed << setprecision(10) << mdist[end] << ' ';
	}
}

int main(void)
{
	int t;
	ios::sync_with_stdio(false);
	cin >> t;
	FOR(i, t){
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << '\n';
	}
}
