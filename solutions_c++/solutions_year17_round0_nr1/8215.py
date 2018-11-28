/*
 * yat0
 * problem A - Small&Large
 */

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, K, len, moves, j;
    string S;

    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	cin >> S >> K;

	len = (int)S.length();
	moves = 0;
	
	for(j=0; j<=(len-K); ++j)
	    if(S[j] == '-')
	    {
		moves++;
		for(int k=0; k<K; ++k)
		    S[j+k] = (S[j+k] == '-') ? '+' : '-';
	    }

	for(int k=len-1; k>=j; --k)
	    if(S[k] == '-')
	    {
		moves = -1;
		break;
	    }

	cout << "Case #" << i << ": ";
	if(moves == -1)
	    cout << "IMPOSSIBLE" << endl;
	else
	    cout << moves << endl;
    }
    
    return 0;
}
