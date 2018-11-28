#include <iostream>
#include <string>
using namespace std;
int main ()
{
int T,K,i,j,iCase=1;
string S;
cin >> T;
while ( T-- )
	{
	cin >> S >> K;
	cout << "Case #" << iCase++ << ": ";
	int iCount = 0 , sSize = S.size();
	for ( i = 0 ; i < sSize - K + 1 ; i ++ )
		{
		if ( S[i] == '-' )
			{
			for ( j = i ; j < i + K ; j ++ )
				S[j] = ( S[j] == '+'  ? '-' : '+' );
			iCount++;
			//cout << iCount << endl;
			}
		}
	for ( i = 0 ; i < sSize ; i ++ )
		if ( S[i] == '-' )
			{
			cout << "IMPOSSIBLE\n";
			break;
			}
	if ( i == sSize )
		cout << iCount << endl;	
	}
}
/*
---+-++- 3
*/
