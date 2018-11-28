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

		for ( int j = int(str.length())-2; j >= 0; --j )
		{
			if ( str[j] > str[j + 1] )
			{
				for ( int k = j+1; k < int(str.length()); ++k )
					str[k] = '9';
				--str[j];
			}
		}

		cout << "Case #" << i+1 << ": " << stoll(str) << endl;
	}
}

