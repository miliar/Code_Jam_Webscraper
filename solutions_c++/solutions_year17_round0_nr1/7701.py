#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >> n;
	for ( int h = 0; h < n; h++ )
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		int cnt = 0;
		for ( int j = 0; j + k - 1 < s.size(); j++ )
		{
			if ( s[j] == '-' ) 
			{
				for ( int i = 0; i < k; i++ )
					if ( s[j+i] == '-' )
						s[j+i] = '+';
					else
						s[j+i] = '-';
				cnt++;
			}			
		}

		for ( int j = 0; j < s.size(); j++ )
			if ( s[j] == '-' )
			{
				cnt = -1;
				break;
			}

			cout << "Case #" << h+1 << ": ";
			if ( cnt == -1 )
				cout << "IMPOSSIBLE";
			else
				cout << cnt;
			cout << endl;	
	}
	return 0;
}