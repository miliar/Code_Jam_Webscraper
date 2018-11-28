#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MAXN = 1024;

int n, k;
bool u[MAXN];

void read()
{
	scanf ( "%d %d", &n, &k );
}

bool check ( int num )
{
	int prev = 10;

	while ( num > 0 ) 
	{
		int dig = num % 10;

		if ( dig > prev ) 
			return false;

		num /= 10;
		prev = dig;

	}

	return true;

}

int findLeft ( int pos )
{
	int count = 0;
	for ( int i = pos - 1; i >= 0; -- i )
	{
		if ( u[i] == 1 ) 
			return count;

		count ++;
	}

	return count;
}

int findRight ( int pos )
{
	int count = 0;
	for ( int i = pos + 1; i <= n; ++ i )
	{
		if ( u[i] == 1 ) 
			return count;

		count ++;
	}

	return count;
}

void solve_small(int test)
{
	memset ( u, 0, sizeof u );

	read();

	u[0] = u[n + 1] = 1;

	int lastLeft = 0, lastRight = 0;
	int lastLeft1 = 0, lastRight1 = 0;
	for ( int i = 0; i < k; ++ i )
	{
		int mx = -1, idx = -1;
		int mx1 = -1, idx1 = -1;
		bool flag = 0;
		for ( int j = 1; j <= n; ++ j )
		{
			if ( u[j] == 1 ) continue; 

			int left = findLeft ( j );
			int right = findRight ( j );

			if ( min ( left, right ) > mx )
			{
				flag = 0;
				mx = min ( left, right );
				lastLeft = left;
				lastRight = right;
				idx = j;
			}
			else if ( min ( left, right ) == mx )
			{
				if ( max ( left, right ) > mx1 )
				{
					flag = 1;
					mx1 = max ( left, right );
					lastLeft = left;
					lastRight = right;
					idx1 = j;
				}
			}
		}

		//cout << idx << " " << idx1 << endl;

		if ( !flag ) 
			u[idx] = 1;
		else 
		{
			u[idx1] = 1;
		}
	}

	printf ( "Case #%d: %d %d\n", test, max ( lastLeft, lastRight ), min ( lastLeft, lastRight ) );

}


int main()
{
	freopen ( "C-small-1-attempt2.in" , "r", stdin );
    freopen ( "c.out", "w", stdout );

	int tests;

	scanf ( "%d", &tests );

	for ( int i = 1; i <= tests; ++ i )
		solve_small(i);

	return 0;

}