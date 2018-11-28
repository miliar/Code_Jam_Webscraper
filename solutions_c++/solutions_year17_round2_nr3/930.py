#include<bits/stdc++.h>
using namespace std;
const bool DBG = 0;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int adj[105][105];
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T,N,Q;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> N >> Q;
		if(DBG) cout << "case " << t << ": " << N << " " << Q << endl;
		vpii pony(N);
		for(int i = 0; i < N; i++) {
			cin >> pony[i].first >> pony[i].second;
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				cin >> adj[i][j];
			}
		}
		vpii q(Q);
		for(int i = 0; i < Q; i++) {
			cin >> q[i].first >> q[i].second;
			q[i].first--;
			q[i].second--;
		}

		if(DBG) cout << "Part 1" << endl;
		vector<vector<ll>> a(N, vector<ll>(N, 1e12));
		for(int start = 0; start < N; start++) {
			vector<bool> done(N);
			priority_queue<pair<ll, int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
			pq.push({0, start});
			while(!pq.empty()) {
				auto c = pq.top(); pq.pop();
				if(done[c.second]) continue;
				done[c.second] = true;
				a[start][c.second] = c.first;
				for(int next = 0; next < N; next++) {
					if(done[next]) continue;
					ll dd = adj[c.second][next];
					if(dd == -1) dd = 1e12;
					if(c.first + dd < a[start][next]) {
						pq.push({c.first + dd, next});
					}
				}
			}
		}
		if(DBG) {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					cout << a[i][j] << " ";
				}
				cout << endl;
			}
		}

		if(DBG) cout << "Part 2" << endl;
		vector<vector<double>> a2(N, vector<double>(N, 1e12));
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				//cout << i << " " << j << endl;
				//cout << a2[i][j] << endl;
				//cout << a[i][j] << endl;
				//cout << "asdf: " << (a[i][j] <= pony[i].first) << endl;
				//cout << "asdf: " << (pony[i].second > 0) << endl;
				//cout << "asdf: " << (a[i][j] * 1.0 / pony[i].second) << endl;
				a2[i][j] = (a[i][j] <= pony[i].first && pony[i].second > 0)? a[i][j] * 1.0 / pony[i].second : 1e15;
				//cout << "jkl: " << a2[i][j] << endl;
			}
		}
		if(DBG) {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					cout << a2[i][j] << " ";
				}
				cout << endl;
			}
		}

		for(int k = 0; k < N; k++) {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					a2[i][j] = min(a2[i][j], a2[i][k] + a2[k][j]);
				}
			}
		}

		cout << "Case #" << t << ":";
		for(int i = 0; i < Q; i++) {
			cout << " " << a2[q[i].first][q[i].second];
		}
		cout << endl;
	}

	return 0;
}
