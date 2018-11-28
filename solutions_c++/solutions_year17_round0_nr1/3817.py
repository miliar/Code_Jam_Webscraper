#include <iostream>
#include <string>

using namespace std;

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		string s;
		int res = 0, k;
		cin >> s >> k;
		for( int i = 0; i + k <= s.length(); i++ ){
			if( s[i] == '-' ){
				res++;
				for( int j = i; j < i + k; j++ )
					s[j] = ( s[j] == '-' ) ? '+' : '-';
			}
		}
		for( int i = 0; i < s.length(); i++ )
			if( s[i] == '-' )
				res = -1;
		cout << "Case #" << T << ": ";
		if( res == -1 )
			cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 0;
}