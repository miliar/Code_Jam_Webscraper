
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1005
#define ones(x) __builtin_popcount(x)

using namespace std;

long long e[N], s[N], d[N][N], floyd[N][N];

struct data{
	
	int id;
	long double d;
	
	data(){}
	data(int _id, long double _d){ id = _id; d = _d; }	
	
};

bool operator <(const data &d1, const data &d2){
	
	return d1.d > d2.d;	
}

long double res[N][N];
int n;

void Dijkstra(int source){
	
	priority_queue<data>Q;
	Q.push(data(source, 0));
	
	for(int i = 0; i < n; i++)res[source][i] = -1;
	res[source][source] = 0;
	
	data best;
	int u;
	long double temp;
	
	while(!Q.empty()){
		
		best = Q.top();
		Q.pop();
		
		u = best.id;
		
		for(int v = 0; v < n; v++){
			
			if(floyd[u][v] == -1 || floyd[u][v] > e[u])continue;
			temp = (floyd[u][v] * 1.0)/s[u];

			if(res[source][v] == -1 || res[source][v] > res[source][u] + temp){
				
				res[source][v] = res[source][u] + temp;
				Q.push(data(v, res[source][v]));
			}
		}
	}
}


int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
		
	while(tc--){
		
		int q;
		scanf("%d%d", &n, &q);
		
		for(int i = 0; i < n; i++)scanf("%d%d", &e[i], &s[i]);
		
		for(int i  = 0; i < n; i++)
			for(int j = 0; j < n; j++)scanf("%d", &d[i][j]), floyd[i][j] = d[i][j];

		for(int k = 0; k < n; k++){
			
			for(int i = 0; i < n; i++){
				
				for(int j = 0; j < n; j++){
				
					if(floyd[i][k] == -1 || floyd[k][j] == -1)continue;
					if(floyd[i][j] == -1)floyd[i][j] = floyd[i][k] + floyd[k][j];
					else floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j]);
				}	
			}
		}
		
		
		for(int i = 0; i < n; i++)Dijkstra(i);
		printf("Case #%d:", caso++);
		
		int u, v;
		for(int i = 0; i < q; i++){
			
			scanf("%d%d", &u, &v);
			u--;  v--;
			
			printf(" %.6Lf", res[u][v]);	
		}
		puts("");
		
	}


}

