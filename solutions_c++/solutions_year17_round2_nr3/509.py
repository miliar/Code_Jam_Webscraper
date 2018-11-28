#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
#define ld long double
#define sz(a) ((int)(a).size())
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define pii pair<int,int>
#define pdd pair<ld,ld> 
#define rep(i,a,b) for(int i=a; i<b; i++)
#define dec(i,a,b) for(int i=a; i>=b; i--)
#define ler freopen("inspection.in","r",stdin);freopen("inspection.out","w",stdout)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define debug cout<<"!!?!!\n"
#define N 100007
using namespace std;

ll t, n, k;
ll grafo[111][111], dist[111];
ld d[111], s[111];
set <pair<ld,int> > q;
vector <pair<ld,int> > adj[111];

void dij(int ini){
	q.clear();
	clr(dist,-1);
	
	dist[ini]=0;
	q.insert(mp(dist[ini],ini));
	
	int y, x, c;
	while(!q.empty()){
		x= q.begin()->S;
		q.erase(q.begin());
		
		rep(i,0,n){
			if(grafo[x][i]==-1) continue;
			if(grafo[x][i] + dist[x] < dist[i] || dist[i]==-1){
				if(dist[i]!=-1) q.erase(mp(dist[i],i));
				dist[i]= grafo[x][i] + dist[x];
				q.insert(mp(dist[i],i));
			}
		}
	}
	
	rep(i,0,n){
		if(dist[i]>0 && dist[i]<=d[ini]){
			adj[ini].pb(mp(dist[i]*1.L/s[ini],i));
		}
	}
}

ld ans[111];
void solve(int ini){
	q.clear();
	rep(i,0,111) ans[i]=-1;
	
	ans[ini]=0;
	q.insert(mp(ans[ini],ini));
	
	int x, y;
	ld c;
	while(!q.empty()){
		x= q.begin()->S;
		q.erase(q.begin());
		
		rep(i,0,sz(adj[x])){
			y=adj[x][i].S;
			c=adj[x][i].F;
			
			if(ans[y]==-1 || ans[x]+c < ans[y]){
				if(ans[y]!=-1) q.erase(mp(ans[y],y));
				ans[y]= ans[x]+c;
				q.insert(mp(ans[y],y));
			}
		}
	}
}


int main(){
	cin >> t;
	rep(caso,1,t+1){
		cin >> n >> k;
		rep(i,0,n) cin >> d[i] >> s[i];
		rep(i,0,n) rep(j,0,n) cin >> grafo[i][j];
		rep(i,0,n) dij(i);

		
		cout << "Case #" << caso << ": ";
		rep(i,0,k){
			int ini, fim;
			cin >> ini >> fim; ini--; fim--;
			solve(ini);
			cout << setprecision(15) << fixed << ans[fim] << " ";
		}
		cout << endl;
		rep(i,0,111) adj[i].clear();
	}
}












