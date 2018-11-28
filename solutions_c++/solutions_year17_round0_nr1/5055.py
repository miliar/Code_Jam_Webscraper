#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tc, cc = 0;
	for( cin >> tc ; tc -- ; )
	{
		int ans = 0, k;
		string s;
		cin >> s >> k;
		for( int i = 0 ; i + k <= s.size() ; i ++ )
			if( s[i] == '-' )
			{
				for( int j = i ; j < i+k ; j ++ )
					s[j] = ( s[j] == '+' ? '-' : '+' );
				ans ++;
			}
		if( s.find( '-' ) != s.npos )
			cout << "Case #" << ++ cc << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}
