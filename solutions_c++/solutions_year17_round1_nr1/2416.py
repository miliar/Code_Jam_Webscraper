#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int Ntests;
	cin >> Ntests;

	for ( int counter = 0; counter < Ntests; ++counter )
	{
		int R, C;
		cin >> R >> C;

		vector<string> str( R );
		for ( int i=0; i<R; ++i )
		{
			cin >> str[i];
		}

		vector<char> used;
		for ( int i=0; i<R; ++i )
		{
			for ( int j = 0; j < C; ++j )
			{
				if ( str[i][j] != '?' )
				{
					const char curname = str[i][j];
					bool oldname = false;
					for ( auto chr : used )
						if ( curname  == chr )
						{
							oldname = true;
							break;
						}
					if ( oldname )
						continue;

					int jmin, jmax, imin, imax;
					{
						for ( jmin = j; jmin > 0; --jmin )
							if ( str[i][jmin - 1] != '?' )
								break;
						for ( jmax = j; jmax < C - 1; ++jmax )
							if ( str[i][jmax + 1] != '?' )
								break;
						for ( imin = i; imin > 0; --imin )
						{
							bool good_row = true;
							for ( int jj = jmin; jj <= jmax; ++jj )
								if ( str[imin - 1][jj] != '?' )
								{
									good_row = false;
									break;
								}
							if ( ! good_row )
								break;
						}
						for ( imax = i; imax < R - 1; ++imax )
						{
							bool good_row = true;
							for ( int jj = jmin; jj <= jmax; ++jj )
								if ( str[imax + 1][jj] != '?' )
								{
									good_row = false;
									break;
								}
							if ( ! good_row )
								break;
						}
					}

					for ( int ii=imin; ii<=imax; ++ii )
						for ( int jj=jmin; jj<=jmax; ++jj )
							if ( ! ( ii == i && jj == j ) )
								str[ii][jj] = curname;

					used.push_back( curname );
					j = jmax;
					if ( jmin == 0 && jmax+1 == C )
						i = imax;
				}
			}
		}


		cout << "Case #" << counter+1 << ":" << endl;
		for ( int i=0; i<R; ++i )
		{
			for ( int j = 0; j < C; ++j )
				if ( str[i][j] == '?' )
				{
					_ASSERTE(0);
					cout << "ERROR!\n";
					return 1;
				}
			cout << str[i] << std::endl;
		}
	}

	return 0;
}

