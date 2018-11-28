#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int M = 102;

struct node {
	double t;
	int u, v;
	node(double _t = 0, int _u = 0, int _v = 0) {
        t = _t;
        u = _u;
        v = _v;
	}
	bool operator < (const node & a) const {
		return t < a.t || (t == a.t && u < a.u) || (t == a.t && u == a.u && v < a.v);
	}
};

ll F[M][M];
int E[M], S[M], D[M][M], N, Q;
set <node> se;
double T[M][M];

double solve(int u, int v) {
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			T[i][j] = 100000000000000.0;
	T[u][u] = 0;

	se.clear();
	se.insert(node(0, u, u));
	while (!se.empty()) {
		node u = *se.begin();
		se.erase(se.begin());
		if (u.u == v) return u.t;
		ll gone = F[u.v][u.u];
		for (int i = 1; i <= N; i++) {
			if (D[u.u][i] != -1 && gone + D[u.u][i] <= E[u.v]) {
                double t = (double)D[u.u][i]/S[u.v];
                if (T[i][u.v] > T[u.u][u.v] + t) {
                    set<node>::iterator it = se.find(node(T[i][u.v], i, u.v));
                    if (it != se.end()) se.erase(it);
                    T[i][u.v] = T[u.u][u.v] + t;
                    se.insert(node(T[i][u.v], i, u.v));
                }
			}
		}
		if (T[u.u][u.u] > T[u.u][u.v]) {
			set<node>::iterator it = se.find(node(T[u.u][u.u], u.u, u.u));
			if (it != se.end()) se.erase(it);
			T[u.u][u.u] = T[u.u][u.v];
			se.insert(node(T[u.u][u.u], u.u, u.u));
		}
	}
}

int main() {
	freopen("C-large (1).in","r", stdin);
	freopen("output.txt","w", stdout);
	ios::sync_with_stdio(0);
	int t; cin >> t; int te = t;
	while (t--) {
		cin >> N >> Q;
		for (int i = 1; i <= N; i++)
			cin >> E[i] >> S[i];
		memset(F, -1, sizeof F);
		for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++) {
            cin >> D[i][j];
            F[i][j] = D[i][j];
        }
        //
        for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            if (F[k][j] != -1 && F[i][k] != -1)
                F[i][j] = (F[i][j]==-1? F[i][k] + F[k][j] : min(F[i][j], F[i][k] + F[k][j]));
        for (int i = 1; i <= N; i++)
            F[i][i] = 0;
        //
		cout << "Case #" << te-t << ": ";
        while (Q--) {
            int u, v; cin >> u >> v;
            cout << fixed << setprecision(9) << solve(u,v) << " ";
        }
        cout << endl;
    }

	return 0;
}
