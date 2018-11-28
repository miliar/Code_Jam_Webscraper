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
		__int64 nstalls, np;
		cin >> nstalls >> np;

		__int64 _max, _min;
		__int64 numofgaps=1;
		while ( true )
		{
			__int64 smallgapsize = nstalls / numofgaps;
			__int64 numofbiggaps = nstalls % numofgaps;
			__int64 numofsmallgaps = numofgaps - numofbiggaps;
			if ( np == 1 )
			{
				if ( numofbiggaps )
				{
					_max = smallgapsize/2 + smallgapsize%2;
					_min = smallgapsize/2;
				}
				else
				{
					_max = (smallgapsize-1)/2+(smallgapsize-1)%2;
					_min = (smallgapsize-1)/2;
				}
				break;
			}
			else if ( np <= numofbiggaps ) // set of big gaps
			{
				_max = smallgapsize/2 + smallgapsize%2;
				_min = smallgapsize/2;
				break;
			}
			else if ( np <= numofgaps ) // set of small gaps
			{
				_max = (smallgapsize-1)/2+(smallgapsize-1)%2;
				_min = (smallgapsize-1)/2;
				break;
			}
			else // next turn
			{
				np -= numofgaps;
				nstalls -= numofgaps;
			}
			numofgaps *= 2;
		}

		cout << "Case #" << i+1 << ": " << _max << " " << _min << endl;
	}
}

