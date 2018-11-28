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
	int t, k, n, test = 1;
	freopen("A-large.in", "r", stdin );
	freopen("A-large.sol", "w", stdout );
	char s[1010];
	scanf("%d", &t );
	while( t-- ){
		
		scanf("%s %d", s, &k );
		n = strlen(s);
		bool aux = 0;
		int cnt = 0;
		rep( i, 0, n ){
			if( s[i] != '-' ) continue;
			if( i > n-k ){
				aux = 1;
				break;
			}
			cnt++;
			rep( j, i, i+k ) s[j] = ( s[j] == '-') ? '+' : '-';	
//			debug(s)
		}
		if( aux ) printf("Case #%d: IMPOSSIBLE\n", test++ );
		else printf("Case #%d: %d\n", test++, cnt++ );
	}
}

