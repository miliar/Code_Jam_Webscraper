#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for(int i = int(a); i < int(b); i++)
#define it(i, a)  for( typeof( a.begin() ) i = a.begin(); i != a.end(); i++ )
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " = " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) cout << x[i][j] << " "; printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define MAXV 1010000
#define F first
#define S second
#define EPS 1e-9
#define mk make_pair

using namespace std;

typedef pair <int, int> ii;
typedef long long int ll;
	
int n, q;
double dist[100][100];
int mat[100][100];

int dijkstra( int ini, int e, double v ){
	priority_queue< pair<double,ii> > pq;
	vector<double> D(100, INF);
	D[ini] = 0; 
	pq.push( mk( 0, ii( ini, e ) ) );
	while( !pq.empty() ){
		int u = pq.top().S.F;
		e = pq.top().S.S;
		double d = -pq.top().F;
		pq.pop();
		if( fabs( D[u] - d ) > EPS ) continue;
		dist[ini][u] = min( dist[ini][u], d );
		rep( i, 0, n ){
			if( mat[u][i] == -1 ) continue;
			double d_u_i = mat[u][i]/v;
			if( D[i] > D[u] + d_u_i && e >= mat[u][i] ){
				D[i] = D[u] + d_u_i;
				pq.push( mk( -D[i], ii( i, e - mat[u][i] ) ) );
			}
		}
		
	} 
}

int main(){

	int t, teste = 1, e[100], s[100], a, b;
	scanf("%d", &t );
	while( t-- ){
		scanf("%d%d", &n, &q );
		rep( i, 0, n )
			rep( j, 0, n )
				dist[i][j] = ( i != j ) * 1LL << 60;
		rep( i, 0, n ){
			scanf("%d%d", &e[i], &s[i] );
		}
		rep( i, 0, n ) rep( j, 0, n ) scanf("%d", &mat[i][j] );
		rep( i, 0, n ) dijkstra( i, e[i], s[i] );
		rep( k, 0, n ) rep( i, 0, n ) rep( j, 0, n ) dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j] );
		printf("Case #%d:", teste++ );
		while( q-- ){
			scanf("%d%d", &a, &b );
			printf(" %.8f", dist[a-1][b-1] );
		}
		printf("\n" );
	}

}
