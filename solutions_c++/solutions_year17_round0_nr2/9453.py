#include <iostream>
#include <string>
using namespace std;
string sub ( string s )
	{
	if ( s == "1" )
		return "";
	if ( s[s.size() - 1] != '0' )
		s[s.size() - 1] -= 1;
	else
		s = sub(s.substr(0,s.size()-1)) + '9';
	return s;
	}
int main ()
{
int T,i,j,iCase=1;
cin >> T;
while ( T-- )
	{
	string N;
	cin >> N;
	cout << "Case #" << iCase++ << ": ";
	while ( N != "0" )
		{
		for ( i = 0 ; i < N.size()-1 ; i ++ )
			if ( N[i] > N[i+1] )
				break;
		if ( i == N.size() - 1 )
			{
			cout << N << endl;
			break;
			}
		N = sub(N);
		}
	}
}
/*
---+-++- 3
*/
