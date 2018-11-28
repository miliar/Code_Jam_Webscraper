//touch {a..m}.in; tee {a..m}.cpp < template.cpp
#include <bits/stdc++.h>
using namespace std;
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define pb push_back
#define RND(a, b) (rand()%((b)-(a)+1)+(a))
#define fst first
#define snd second
typedef long long ll;
typedef pair<double,int> ii;
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define dprint(v) cout << #v"=" << v << endl //;)
const double EPS=1e-9;
const int MAXN=110;
int N, Q;
ll E[MAXN], S[MAXN];
ll D[MAXN][MAXN];
double dist[MAXN][MAXN];
const ll INF =1e18;

void dijkstra(int s, double *dist){//O(|E| log |V|)
	priority_queue<ii, vector<ii>, greater<ii> > Q;
	forn(i, N) dist[i]=INF;
	Q.push(make_pair(0, s)); dist[s] = 0;
	while(sz(Q)){
		ii p = Q.top(); Q.pop();
        forn(i, N){
            double x=D[p.snd][i];
            if(x<=E[p.snd]+EPS){
                double t=x/(double)S[p.snd];
                if(dist[p.snd]+t < dist[i]){
                    dist[i] = dist[p.snd] + t;
                    Q.push(make_pair(dist[i], i));
                }
            }
            
        }
	}
}



void solve(){
    cin >> N >> Q;
    forn(i, N){
        cin >> E[i] >> S[i];
    }
    //~ dprint(N), dprint(Q);
    forn(i, N) forn(j, N){
        cin >> D[i][j];
        if(D[i][j]==-1) D[i][j]=INF;
    }
    forn(k, N) forn(i, N) if(D[i][k]!=INF) forn(j, N) if(D[k][j]!=INF)
        D[i][j]=min(D[i][j], D[i][k]+D[k][j]);
    forn(i, N) dijkstra(i, dist[i]);
    forn(qq, Q){
        int U, V; cin >> U >> V; U--, V--;
        if(qq) cout << ' ';
        if(dist[U][V]==INF) cout << -1;
        else cout << dist[U][V];
    }
    cout << endl;
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("c.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    cout << setprecision(9) << fixed;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        solve();
    }
    return 0;
}
