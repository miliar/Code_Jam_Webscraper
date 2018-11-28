#include <bits/stdc++.h>
using namespace std;

const int maxn = 111;
double timeTaken[maxn][maxn];
long long fw[maxn][maxn];
vector<int> edges[maxn];
const long long inf = (1LL << 60);

int E[maxn], S[maxn];

void init(){
    for(int i = 0; i < maxn; i++)
	edges[i].clear();
}

priority_queue< pair<double, pair<int,int> >, vector< pair<double, pair<int,int> > >, greater< pair<double, pair<int,int> > > > pq;

void dijkstra(int source, int n){
    for(int i = 1; i <= n; i++)
	for(int j = 1; j <= n; j++)
	    timeTaken[i][j] = inf;
    timeTaken[source][source] = 0;
    pq.push( make_pair(0, make_pair(source, source)) );
    while(!pq.empty()){
	pair<double, pair<int,int> > ele = pq.top();
	pq.pop();
	int horse = ele.second.second;
	int u = ele.second.first;
	double dist = ele.first;

	for(int v = 1; v <= n; v++){
	    if(fw[u][v] >= inf) continue;
	    if(u == v) continue;
	    if(fw[horse][v] > E[horse]) continue;
	    double add = fw[u][v] / (1.0 * S[horse]);
	    add += dist;

	    if(add < timeTaken[v][horse]){
		timeTaken[v][horse] = add;
		pq.push( make_pair(add, make_pair(v,horse) ) );
	    }

	    if(add < timeTaken[v][v]){
		timeTaken[v][v] = add;
		pq.push( make_pair(add, make_pair(v, v)) );
	    }
	}
    }
}

void solve(){
    int n, q;
    cin >> n >> q;

    for(int i = 1; i <= n; i++)
    	cin >> E[i] >> S[i];

    for(int i = 1; i <= n; i++){
	for(int j = 1; j <= n; j++){
	    cin >> fw[i][j];
	    if(fw[i][j] < 0)
		fw[i][j] = inf;
	    else
		edges[i].push_back(j);
	    if(i == j) fw[i][j] = 0;
	}
    }

    for(int k = 1; k <= n; k++)
	for(int i = 1; i <= n; i++)
	    for(int j = 1; j <= n; j++)
		fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j]);

    while(q--){
	int u,v;
	cin >> u >> v;
	dijkstra(u, n);
	double ans = inf;
	for(int h = 1; h <= n; h++)
	    ans = min(ans, timeTaken[v][h]);
	printf("%.6lf ", ans);
    }
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
	cout << "Case #" << i << ": ";
	solve();
	printf("\n");
    }
    return 0;
}
