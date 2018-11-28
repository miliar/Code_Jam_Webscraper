#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define For(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define len(arr) ((int)(arr).size())

typedef long long ll;

const ll LL_INF = 1e18;

struct Node {
	ll E, S;
};

const int MAX_N = 110;

ll dist[MAX_N][MAX_N];
double travel_time[MAX_N][MAX_N];

void solve() {
	cout.precision(8);
	cout << fixed;

	int N, Q;
	cin >> N >> Q;
	vector<Node> nodes(N);
	For(i, N)
		cin >> nodes[i].E >> nodes[i].S;
	For(i, N) For(j, N) {
		ll D;
		cin >> D;
		dist[i][j] = (D == -1) ? LL_INF : D;
	}

	For(k, N) For(i, N) For(j, N)
		dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

	For(i, N) For(j, N) {
		if (nodes[i].E >= dist[i][j])
			travel_time[i][j] = (double) dist[i][j] / nodes[i].S;
		else
			travel_time[i][j] = LL_INF;
	}

	For(k, N) For(i, N) For(j, N)
		travel_time[i][j] = min(travel_time[i][j], travel_time[i][k] + travel_time[k][j]);

	For(i, Q) {
		int U, V;
		cin >> U >> V;
		U--;
		V--;

		cout << travel_time[U][V] << ' ';
	}
	cout << '\n';
}

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
		cout << "Case #" << no << ": ";
		solve();
	}
	return 0;
}
