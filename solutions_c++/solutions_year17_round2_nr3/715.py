//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ALL(G) (G).begin(),(G).end()

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000009;
const int MAXN = 100;

int n, q, source, dest;
int E[MAXN + 3], S[MAXN + 3];
LL D[2][MAXN + 3][MAXN + 3];
double Adj[2][MAXN + 3][MAXN + 3];
double dist[MAXN + 3][MAXN + 3];

int Floyd(){
    int e = 0, f = 1;
    
    for(int k=1; k<=n; k++){
		for(int i=1; i<=n; i++) 
			for(int j=1; j<=n; j++){
				D[f][i][j] = min(D[e][i][j], D[e][i][k] + D[e][k][j]);
			}
		swap(e, f);
    }
    
    return e;
}

int Floyd2(){
    int e = 0, f = 1;
    
    for(int k=1; k<=n; k++){
		for(int i=1; i<=n; i++) 
			for(int j=1; j<=n; j++){
				Adj[f][i][j] = min(Adj[e][i][j], Adj[e][i][k] + Adj[e][k][j]);
			}
		swap(e, f);
    }
    
    return e;
}

void Read(){
	scanf("%d %d", &n, &q);
	for(int i=1; i<=n; i++)
		scanf("%d %d", &E[i], &S[i]);
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++){
			scanf("%lld", &D[0][i][j]);
			if(D[0][i][j] == -1)
				D[0][i][j] = INF;
		}
	
	
}

void Solve(){
	int e = Floyd();
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++){
			if(D[e][i][j] <= E[i])
				Adj[0][i][j] = (double)D[e][i][j]/S[i];
			else
				Adj[0][i][j] = 1e18;
		}
	e = Floyd2();
	
	for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
			dist[i][j] = Adj[e][i][j];
}

int main(){
    int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		Read();
		Solve();
		printf("Case #%d: ", pp);
		while(q--){
			int a, b;
			scanf("%d %d", &a, &b);
			printf("%.10lf ", dist[a][b]);
		}
		puts("");
	}
    
return 0;
}