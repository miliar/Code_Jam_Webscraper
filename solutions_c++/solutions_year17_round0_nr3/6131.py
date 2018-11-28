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

typedef long long int ll;
typedef pair <ll, ll> ii;

ii ans;

void solve( ll i, ll j, ll k ){
	ll mid = (i+j)/2;
	if( !k ) return;
	if( k == 1 ){
		ans = min( ans, ii( max( mid - i, 0LL ), max( j - mid, 0LL ) ) );
		return;
	}
	k--;
	solve( i, mid-1, k/2 );
	solve( mid+1, j, (k+1)/2 );
}

int main(){
	ll t, test = 1, n, k;
	freopen("C-small-2-attempt0.in", "r", stdin );
	freopen("C-small-2-attempt0.sol", "w", stdout );

	scanf("%lld", &t );
	while( t-- ){
		scanf("%lld%lld", &n, &k );
		ans = ii( n, n );
		if( n == k ) ans = ii( 0, 0 );
		else solve( 1, n, k );
		printf("Case #%lld: %lld %lld\n", test++, max( ans.F, ans.S ), min( ans.F, ans.S ) );
	}
}

