#include <bits/stdc++.h>
#define endl '\n'
#define forn(i, n) for(int i=0;i<n;i++)
#define lli long long int
#define pii pair<lli,lli>
#define psi pair<double,pii>
#define fi first
#define se second
#define pb push_back

using namespace std;

const int MAXN = 101;

pii num[MAXN];
bool used[MAXN];
lli mat[MAXN][MAXN];

double D(int s,int t,int n) {
	queue<int> pos;
	pos.push(s);
	vector<double> dist(n, 1E50);
	dist[s] = 0.0;

	while(!pos.empty()) {
		s = pos.front();
		pos.pop();

		priority_queue<psi, vector<psi>, greater<psi> > q;
		q.push( psi(dist[s], pii(0, s)) );

		lli limi = num[s].fi;
		double vel = num[s].se;

		while(!q.empty()) {
			int u = q.top().se.se;
			double tiempo = q.top().fi;
			lli d = q.top().se.fi;
			
			q.pop();

			if(tiempo > dist[u]) continue;

			forn(i, n) {
				double mas = mat[u][i] / vel;
				if(tiempo + mas < dist[i] && d + mat[u][i] <= limi) {
					dist[i] = tiempo + mas;
					q.push(psi(dist[i], pii(d + mat[u][i], i)));
				}
			}
		}

		double mini = 1E50;
		int id;
		forn(i, n) 
			if(!used[i] && mini > dist[i]) {
				mini = dist[i];
				id = i;
			}

		if(mini < 1E50) {
			pos.push(id);
			used[id] = 1;
		}
	}

	return dist[t];
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout<<fixed<<setprecision(9);
	int t,u,v,n,q,caso = 1;
	cin>>t;
	while(t--) {
		cin>>n>>q;
		forn(i, n) cin>>num[i].fi>>num[i].se;

		forn(i, n)
		forn(j, n) {
			cin>>mat[i][j];
			if(mat[i][j] == -1) mat[i][j] = 1LL<<60;
		}

		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
			    for (int j = 0; j < n; ++j)
				mat[i][j] = min(mat[i][j],
				    mat[i][k] + mat[k][j]);

		cout<<"Case #"<<caso++<<":";
		while(q--) {
			cin>>u>>v;
			u--,v--;
			forn(i, n) used[i] = 0;
			cout<<" "<<D(u, v, n);
		}
		cout<<endl;
	}
	return 0;
}
