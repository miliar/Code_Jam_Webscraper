#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 100005;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

int Hp, Att, HpE, AttE, Buff, Deb;

void preprocessing()
{
	scanf( "%d%d%d%d%d%d", &Hp, &Att, &HpE, &AttE, &Buff, &Deb );
}

void solve()
{
	int ret = Inf;
	fo ( cnB, 0, HpE+1 ) 
	{
		if ( !Buff && cnB ) continue;
		fo ( cnD, 0, Hp+1 )
		{
			if ( !Deb && cnD ) continue;
			int hp = Hp, at = Att, hpe = HpE, ate = AttE;
			int cB = 0, cD = 0;
			fo ( step, 0, 1000 )
			{
				if ( at>=hpe )  // kill out
				{
					ret = min( ret, step+1 );
					break;
				}
				if ( hp<=ate && !( cD<cnD && hp>ate-Deb ) )  // cure
				{
					hp = Hp - ate;
					continue;
				}
				// free to do any move
				if ( cD<cnD ) ate = max( ate-Deb, 0 ), ++cD;
				else if ( cB<cnB ) at += Buff, ++cB;
				else hpe -= at;
				hp -= ate;
			}
		}
	}
	if ( ret==Inf ) printf( "IMPOSSIBLE\n" );
	else printf( "%d\n", ret );
}

int main()
{
	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		printf( "Case #%d: ", Case+1 );
		preprocessing(); 
		solve();
	}
	return 0;
}

