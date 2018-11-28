#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e2 + 10;
typedef long long i64;




int E[MAX], S[MAX];
int g[MAX][MAX];
struct rider{
	int h;
	int v;
	int kilo;
	double tt;
	bool operator<(const rider& a)const{
		return tt > a.tt;
	}
};
priority_queue<rider> que;
double dist[MAX][MAX];

double ans[MAX][MAX];
int N;
void dijkstra(int v){
	que = priority_queue<rider>();
	for(int i = 0; i <N; i++)
		for(int j = 0; j <N; j++)
			dist[i][j] = -1;
	que.push((rider){v, v, 0, 0});
	dist[v][v] = 0;
	while(!que.empty()){
		auto cur = que.top();
		que.pop();
		if(dist[cur.h][cur.v] < cur.tt)continue;

		for(int i = 0; i < N; i++){
			if(g[cur.v][i] == -1)continue;
			if(E[cur.h] - cur.kilo < g[cur.v][i]) continue;
			rider nn;
			nn.v = i;
			nn.h = cur.h;
			nn.kilo = cur.kilo + g[cur.v][i];
			nn.tt = cur.tt + (double)g[cur.v][i] / S[cur.h];
			if(dist[cur.h][i] == -1 or (dist[cur.h][i] > nn.tt)){
				dist[cur.h][i] = nn.tt;
				que.push(nn);
			}
			nn.h = i;
			nn.kilo = 0;
			if(dist[nn.h][i] == -1 or (dist[nn.h][i] > nn.tt)){
				dist[nn.h][i] = nn.tt;
				que.push(nn);
			}

		}
	}
	for(int i = 0; i < N; i++)ans[v][i] = 1e18;
	for(int i = 0; i < N; i++)

		for(int j = 0 ;j < N; j++){
			if(dist[i][j] == -1)continue;
			ans[v][j] = min(ans[v][j], dist[i][j]);
		}

}


int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'

    int T; cin >> T;
    for(int tt = 0; tt < T; tt++){
    	cout << "Case #" << tt + 1 << ": ";
    	int  Q; cin >> N >> Q;
    	for(int i = 0; i < N; i++)cin >> E[i] >> S[i];
    	for(int i = 0; i < N; i++)
    		for(int j = 0; j < N; j++)
    			cin >> g[i][j];
    	for(int i = 0; i < N; i++)
    		dijkstra(i);
    	while(Q--){
    		int u, v; cin >> u >> v;u--, v--;
    		cout << fixed << setprecision(8) << ans[u][v] << (Q == 0 ? '\n' : ' ');
    	}

    }

}

