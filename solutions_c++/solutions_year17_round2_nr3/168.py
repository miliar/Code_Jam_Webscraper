#include<bits/stdc++.h>
#define LIM 111

using namespace std;

long long s[LIM] , e[LIM] , dist[LIM][LIM];
double t[LIM][LIM];
int n,q;

const long long inf = 1e15;
const double INF = 1e15;

void solve(int Tc){
	cin>>n>>q;
	for(int i = 1 ; i <= n ; i++) cin>>e[i]>>s[i];
	for(int u = 1 ; u <= n ; u++)
		for(int v = 1 ; v <= n ; v++){
			long long x;
			cin>>x;
			dist[u][v] = (x == -1 ? inf : x);
			if(u == v)	dist[u][v] = 0;
		}
	for(int k = 1 ; k <= n ; k++)
		for(int u = 1 ; u <= n ; u++)
			for(int v = 1 ; v <= n ; v++)
				dist[u][v] = min(dist[u][v] , dist[u][k] + dist[k][v]);
	for(int u = 1 ; u <= n ; u++)
		for(int v = 1 ; v <= n ; v++){
			if(u == v)	t[u][v] = 0;
			else{
				if(dist[u][v] > e[u])	t[u][v] = INF;
				else t[u][v] = (double) dist[u][v] / (double) s[u];	
			}
		}
	for(int k = 1 ; k <= n ; k++)
		for(int u = 1 ; u <= n ; u++)
			for(int v = 1 ; v <= n ; v++)
				t[u][v] = min(t[u][v] , t[u][k] + t[k][v]);
	printf("Case #%d: ",Tc);
	while(q > 0){
		int u , v;
		cin>>u>>v;
		printf("%.10lf ",t[u][v]);
		q--;
	}
	printf("\n");
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++)	solve(i);
}
