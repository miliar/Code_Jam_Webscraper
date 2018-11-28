#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

vector<pair<int, ll> > g[110];
double tmin[110][110];
ll maxDist[110];
ll speed[110];
int n, q;

double dij(int o, int d){
	for(int i=0; i<n; i++){
		for (int j = 0; j < n; j++)
		{
			tmin[i][j] = 1000000000000000000000000.0;
		}
		
		
	
	}
	priority_queue<pair<double, pair<ll, pair<int, int> > >, vector< pair<double, pair<ll, pair<int, int> > > >, greater<pair<double, pair<ll, pair<int, int> > > >  > pq;
	pq.push(mp(0.0, mp(0, mp(o, o))));
	tmin[o][o] = 0.0;
	pair<double, pair<ll, pair<int, int> > > p;
	
	ll dist;
	int u, cavalo;
	double t;
	ll w;
	int v;
	double tt;
	
	while (!pq.empty())
	{
		p = pq.top();
		pq.pop();
		
		t = p.F;
		dist = p.S.F;
		u = p.S.S.F;
		cavalo = p.S.S.S;
		if(p.F > tmin[p.S.S.F][cavalo]) continue;
		
		
		
		
		
		for (int i = 0; i < g[u].size(); i++)
		{
			v = g[u][i].F;
			w = g[u][i].S;
			
			//atual
			if(dist+w <= maxDist[cavalo]){
				tt = w*1.0 / speed[cavalo]*1.0;
				if(tmin[u][cavalo] + tt < tmin[v][cavalo]){
					tmin[v][cavalo] = tmin[u][cavalo] + tt;
					pq.push(mp(tmin[v][cavalo], mp(dist+w, mp(v, cavalo))));
				}
			}
			if(u!=o && w <= maxDist[u]){
				tt = w*1.0 / speed[u]*1.0;
				if(tmin[u][cavalo] + tt < tmin[v][u]){
					tmin[v][u] = tmin[u][cavalo] + tt;
					pq.push(mp(tmin[v][u], mp(w, mp(v, u))));
				}
			}
		}
		
	}
	double ans = 100000000000000000000000000.0;
	for (int i = 0; i < n; i++)
	{
		ans = min(ans, tmin[d][i]);
	}
	
	return ans;
}

void reset(){
	for (int i = 0; i < n; i++)
	{
		g[i].clear();
	}
	
}

int main () {

	int t,u, v;
	cin >> t;
	for(int tc=1; tc<=t; tc++){
		cin >> n >> q;
		reset();
		for (int i = 0; i < n; i++)
		{
			cin >> maxDist[i] >> speed[i]; 
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				int x;
				cin >> x;
				if(x!=-1) g[i].pb(mp(j, x));
			}
		}
		
		vector<double> saida;
		for (int i = 0; i < q; i++)
		{
			cin >> u >> v;
			u--; v--;
			saida.pb(dij(u, v));
		}
		cout << "Case #" << tc << ": ";
		cout << fixed << setprecision(10);
		for (int i = 0; i < saida.size(); i++)
		{
			cout << saida[i] << " ";
		}
		cout << "\n";
		
	}
	
	return 0;
}
