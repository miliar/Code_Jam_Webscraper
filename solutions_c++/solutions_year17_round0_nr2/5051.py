#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
vector < LL > a;

void f( LL x, int len )
{
	if( len > 18 )
		return;
	a.push_back( x );
	for( int i = (x%10) ; i < 10 ; i ++ )
		f( x * 10 + i, len + 1 );
}

int main()
{
	int tc, cc = 0;
	f( 0, 0 );
	sort( a.begin(), a.end() );
	for( cin >> tc ; tc -- ; )
	{
		LL n;
		cin >> n;
		int l = 0, r = a.size();
		while( l+1 < r )
		{
			int m = ( l + r ) / 2;
			if( a[m] <= n )
				l = m;
			else
				r = m;
		}
		cout << "Case #" << ++cc << ": " << a[l] << endl;
	}
	return 0;
}
