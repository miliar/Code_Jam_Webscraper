#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for(int i = int(a); i < int(b); i++)
#define pb push_back
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " = " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) cout << x[i][j] << " "; printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define F first
#define S second
#define mk make_pair

using namespace std;

typedef pair <int, int> ii;
typedef long long int ll;

int main(){
	
	freopen("A.in", "r", stdin );
	freopen("A.sol", "w", stdout );
	
	int t, n, p, aux, v[10];
	scanf("%d", &t );
	rep( test, 1, t+1 ){
		scanf("%d%d", &n, &p );
		memset( v, 0, sizeof v );
		rep( i, 0, n ){
			scanf("%d", &aux );
			v[aux%p]++;
		}
		printf("Case #%d: ", test );
		if( p == 2 ){
			printf("%d\n", v[0] + ( v[1]+1 )/2 );
		}
		if( p == 3 ){
			int aux = min( v[1], v[2] );
			v[1] -= aux, v[2] -= aux;
			printf("%d\n", v[0] + aux + ( v[1]+2 )/3  + ( v[2] + 2 )/3 );
		}
		if( p == 4 ){
			int aux = min( v[1], v[3] );
			v[1] -= aux, v[3] -= aux;
			if( v[2]&1 ){
				if( v[1] > 2 ) v[1]-=2, aux++, v[2]--;
				else if( v[3] > 2 ) v[3]-=2, aux++, v[2]--;
			}
			printf("%d\n", v[0] + aux + ( v[1]+3 )/4  + (v[2]+1)/2 + (v[3]+3)/4 );
		}
	}
	
	return 0;
}
