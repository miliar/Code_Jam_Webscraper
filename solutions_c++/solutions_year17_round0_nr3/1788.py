#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream input( "input.txt" );
	ofstream output( "output.txt" );
	int T; input >> T;
	for ( int c = 1; c <= T; ++c )
	{
		long long n; input >> n;
		long long k; input >> k;
		while ( true )
		{
			long long ls = ( n - 1 ) / 2;
			long long lr = n - 1 - ls;
			if ( k == 1 )
			{
				output << "Case #" << c << ": " << lr << " " << ls << endl;
				break;
			}
			n = (k % 2 == 0) ? lr : ls;
			k = k / 2;
		}
	}
	input.close();
	output.close();
	cout << "\ndone";
	cin >> T;
}