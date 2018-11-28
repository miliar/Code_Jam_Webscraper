
#define HEADER_H
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ull          = unsigned long long;
using ll           = long long;
using ld           = long double;
using vi           = vector<ll>;
using vvi          = vector<vi>;
using vb           = vector<bool>;
using ii           = pair<ll, ll>;
constexpr bool LOG = true;
void Log() {
	if(LOG) cerr << "\n";
}
template <class T, class... S>
void Log(T t, S... s) {
	if(LOG) cerr << t << "\t", Log(s...);
} /* ============== END OF HEADER ============== */

// adj should be a V*V array s.t. adj[i][j] contains the weight of
// the edge from i to j, INF if it does not exist.
// set adj[i][i] to 0; and always do adj[i][j] = min(adj[i][j], w)

ll adj[100][100];
double adj2[100][100];

void floyd_warshall(ll V) {
	for(ll b = 0; b < V; ++b)
		for(ll a = 0; a < V; ++a)
			for(ll c = 0; c < V; ++c)
				if(adj[a][b] != -1 && adj[b][c] != -1) {
					if(adj[a][c] == -1)
						adj[a][c] = adj[a][b] + adj[b][c];
					else
						adj[a][c] = min(adj[a][c], adj[a][b] + adj[b][c]);
				}
}

void floyd_warshall2(ll V) {
	for(ll b = 0; b < V; ++b)
		for(ll a = 0; a < V; ++a)
			for(ll c = 0; c < V; ++c)
				if(adj2[a][b] >= -0.5 && adj2[b][c] >= -0.5) {
					if(adj2[a][c] < -0.5)
						adj2[a][c] = adj2[a][b] + adj2[b][c];
					else
						adj2[a][c] = min(adj2[a][c], adj2[a][b] + adj2[b][c]);
				}
}

void print_adj(int n) {
	for(int r = 0; r < n; ++r) {
		for(int c = 0; c < n; ++c) cerr << adj[r][c] << '\t';
		cerr << endl;
	}
}
void print_adj2(int n) {
	for(int r = 0; r < n; ++r) {
		for(int c = 0; c < n; ++c) cerr << adj2[r][c] << '\t';
		cerr << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":";
		int n;
		cin >> n;
		int q;
		cin >> q;

		vi max_dist(n), speed(n);
		for(int i = 0; i < n; ++i) cin >> max_dist[i] >> speed[i];

		for(int r = 0; r < n; ++r)
			for(int c = 0; c < n; ++c) {
				cin >> adj[r][c];
			}

		// Log("adj input");
		// if(LOG) print_adj(n);
		floyd_warshall(n);
		// Log("adj processed");
		// if(LOG) print_adj(n);

		// process horses
		for(int s = 0; s < n; ++s) {
			for(int t = 0; t < n; ++t) {
				if(adj[s][t] <= max_dist[s] && adj[s][t] >= 0)
					adj2[s][t] = adj[s][t] / double(speed[s]);
				else
					adj2[s][t] = -1;
			}
		}

		// Log("speeds before");
		// if(LOG) print_adj2(n);
		floyd_warshall2(n);
		// Log("speeds after");
		// if(LOG) print_adj2(n);

		// queries
		while(q--) {
			int s, t;
			cin >> s >> t;
			--s, --t;

			cout << ' ' << setprecision(15) << adj2[s][t];
		}
		cout << endl;
	}
	return 0;
}
