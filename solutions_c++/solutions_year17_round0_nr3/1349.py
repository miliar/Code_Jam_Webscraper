#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		unsigned long long n, k;
		cin >> n >> k;
		while( k > 1 )
		{
			if( n % 2 == 1 )
			{
				n /= 2;
				k--;
				k = k / 2 + k % 2;
			}
			else
			{
				n /= 2;
				n -= k % 2;
				k = k / 2;

			}
		}
		unsigned long long y = n / 2;
		unsigned long long z = n / 2 - 1 + ( n % 2 );
		cout << "Case #" << to_string( t ) << ": " << y << " " << z << endl;
	}
	return 0;
}
