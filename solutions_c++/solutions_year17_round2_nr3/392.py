#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FIL(a,b) memset((a),(b),sizeof(a))
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a),end(a)
#define PB push_back
#define FI first
#define SE second
typedef long long LL;
typedef pair<int,int> PT;
typedef complex<double> PX;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<PT> VPT;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; FOR(i,0,v.size()) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T> const& p)
{ return s << '(' << p.first << ',' << p.second << ')'; }

int TC, N, Q, E[100], S[100], adj[100][100];

struct PQP {
	double t;
	int n, m;
	bool operator<(const PQP& pqp) const {
		return t > pqp.t;
	}
};

double proc(int u, int v) {
	double times[100][100];
	LL dists[100][100];
	FOR(i,0,100) FOR(j,0,100) {
		dists[i][j] = -1;
		times[i][j] = -1.0;
	}

	double ans = 1e100;
	priority_queue<PQP> pq;
	dists[u][u] = 0;
	times[u][u] = 0.0;
	pq.push(PQP{0.0, u, u});
	while (!pq.empty()) {
		PQP pqp = pq.top();
		pq.pop();

		double trv = times[pqp.n][pqp.m];
		if (trv != pqp.t) continue;
		if (pqp.n == v) ans = min(ans, trv);

		//printf("Got to [%d][%d] time %.10f\n", pqp.n, pqp.m, pqp.t);

		FOR(x,0,N) {
			if (adj[pqp.n][x] != -1) {
				LL new_dist = dists[pqp.n][pqp.m] + LL(adj[pqp.n][x]);
				if (new_dist <= E[pqp.m]) {
					double ntrv = trv + double(adj[pqp.n][x]) / S[pqp.m];
					if (times[x][pqp.m] == -1.0 || times[x][pqp.m] > ntrv) {
						times[x][pqp.m] = ntrv;
						dists[x][pqp.m] = new_dist;
						pq.push(PQP{ntrv, x, pqp.m});
					}
					if (times[x][x] == -1.0 || times[x][x] > ntrv) {
						times[x][x] = ntrv;
						dists[x][x] = 0;
						pq.push(PQP{ntrv, x, x});
					}
				}
			}
		}
	}
	return ans;
}

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> Q;
		FOR(n,0,N) cin >> E[n] >> S[n];
		FOR(n,0,N) FOR(m,0,N) cin >> adj[n][m];
		cout << "Case #" << tc << ":";
		FOR(q,0,Q) {
			int u, v;
			cin >> u >> v; --u; --v;
			cout << fixed << setprecision(10) << " " << proc(u, v);
		}
		cout << endl;
	}
}
