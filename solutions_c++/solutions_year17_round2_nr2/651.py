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

int main(){
	int t, teste = 1;
	int r, o, y, g, b, n, v;
	char rr[] = {"RYB"};
	scanf("%d", &t );
	while( t-- ){
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v );
		printf("Case #%d: ", teste++ );
		vector<ii> aux;
		aux.pb( ii( r, 0 ) );
		aux.pb( ii( y, 1 ) );
		aux.pb( ii( b, 2 ) );
		sort( all(aux) );
		if( aux[0].F + aux[1].F < aux[2].F ){
			printf("IMPOSSIBLE\n");
			continue;
		}
		int first = aux[2].S;
		int last = -1;
		rep( i, 0, n-2 ){
			if( aux[2].S != last ){
				printf("%c", rr[ aux[2].S ] );
				aux[2].F--;
				last = aux[2].S;
			}
			else{
				printf("%c", rr[ aux[1].S ] );
				aux[1].F--;
				last = aux[1].S;
			} 
			sort( all(aux) );
		}
		if( aux[2].S == first ) printf("%c%c\n", rr[aux[2].S], rr[aux[1].S] );
		else  printf("%c%c\n", rr[aux[1].S], rr[aux[2].S] );
		
	}

}










