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
		string str; input >> str;
		bool bContinue = true;
		while ( bContinue )
		{
			bContinue = false;
			for ( int i = 1; i < str.size(); ++i )
			{
				if ( str[i] < str[i - 1] )
				{
					--str[i - 1];
					for ( int j = i; j < str.size(); ++j )
					{
						str[j] = '9';
					}
					bContinue = true;
					break;
				}
			}
		}
		while ( str.size() > 1 && str[0] == '0' )
		{
			for ( int i = 0; i < str.size() - 1; ++i )
			{
				str[i] = str[i + 1];
			}
			str.pop_back();
		}
		output << "Case #" << c << ": " << str << endl;
	}
	input.close();
	output.close();
	cout << "\ndone";
	cin >> T;
}