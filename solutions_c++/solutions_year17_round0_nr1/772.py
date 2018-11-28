#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int Ntests;
	cin >> Ntests;

	for ( int i = 0; i < Ntests; ++i )
	{
		string str;
		cin >> str;
		int flipsize;
		cin >> flipsize;

		int Nflips = 0;
		{
			const int j_end = int( str.length() ) - flipsize + 1;
			for ( int j = 0; j < j_end; ++j )
			{
				if ( str[j] == '-' )
				{
					++Nflips;
					for ( int k = 0; k < flipsize; ++k )
					{
						if ( str[j + k] == '-' )
							str[j + k] = '+';
						else
							str[j + k] = '-';
					}
				}
			}
			for ( int j = j_end; j < int( str.length() ); ++j )
				if ( str[j] == '-' )
					Nflips = -1;

		}

		string res;
		if ( Nflips >= 0 )
			res = to_string(Nflips);
		else
			res = "IMPOSSIBLE";
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
