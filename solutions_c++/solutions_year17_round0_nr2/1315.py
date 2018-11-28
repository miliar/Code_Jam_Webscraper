#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		string s;
		cin >> s;
		s = "0" + s;
		size_t incIndex = 0;
		for( size_t i = 1; i < s.size(); i++ )
		{
			if( s[ i ] > s[ i - 1 ] )
			{
				incIndex = i;
			}
			if( s[ i ] < s[ i - 1 ] )
			{
				s[ incIndex ]--;
				for( size_t j = incIndex + 1; j < s.size(); j++ )
				{
					s[ j ] = '9';
				}
			}
		}
		s = s.substr( s.find_first_not_of( '0' ), s.size() );
		cout << "Case #" + to_string( t ) + ": " + s << endl;
	}
	return 0;
}
