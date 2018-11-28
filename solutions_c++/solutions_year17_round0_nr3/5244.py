#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tc, cc = 0;
	for( cin >> tc ; tc -- ; )
	{
		int n, k;
		cin >> n >> k;
		priority_queue < int > pq;
		pq.push( n );
		int l, r;
		while( k -- )
		{
			int x = pq.top();
			pq.pop();
			l = ( x - 1 ) / 2, r = (x-1) - l;
			if( l > r )
				swap( l, r );
			pq.push( l );
			pq.push( r );
		}
		cout << "Case #" << ++cc << ": " << r << " " << l << endl;
	}
	return 0;
}
