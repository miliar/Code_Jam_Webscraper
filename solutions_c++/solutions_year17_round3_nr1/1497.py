#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < LL, LL > pii;
#define fr first
#define se second
#define PI acos(-1.)
const LL INF = 1000000000LL * 1000000000LL;
#define sq(x) ((x)*1ll*(x))

int n, k;
pii a[1024];
LL dp[1024][1024];

LL f( int ls, int rem )
{
	if( !rem )
		return 0;
	if( ls == n )
		return -INF;
	LL &ret = dp[ls][rem];
	if( ret != -1 )
		return ret;
	ret = 0;
	for( int i = ls+1 ; i <= n ; i ++ )
		ret = max( ret, f( i, rem-1 ) + 2 * a[i].fr * a[i].se + abs( sq( a[i].fr ) - sq( a[ls].fr ) ) );
	return ret;
}

int main()
{
	int tc, cc = 0;
	for( cin >> tc ; tc -- ; )
	{
		cin >> n >> k;
		a[0].fr = a[0].se = 0;
		for( int i = 1 ; i <= n ; i ++ )
			cin >> a[i].fr >> a[i].se;
		sort( a, a+n+1 );
		memset( dp, -1, sizeof dp );
		printf( "Case #%d: %.10lf\n", ++ cc, f( 0, k ) * PI );
	}
	return 0;
}
