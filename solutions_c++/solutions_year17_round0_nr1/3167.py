#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;
int down[2010];
int main()
{
    freopen( "in.txt", "r", stdin);
    freopen( "out.txt", "w", stdout);
	int T, cas = 0;
	cin>>T;
	while ( T -- )
	{
		string s;
		int k, ans = 0;
		cin >> s >> k;
		int flips = 0, no = 0;
		//memset(down, sizeof down, 0);
		for (int j = 0 ;j < s.length();j++) down[j] = 0;
		int i = 0;
		for ( i = 0 ; i <= s.length() - k; i ++ )
        {
            flips -= down[i];
            if ((s[i] == '-') ^ (flips & 1)) {
   //             cout << s[i] << " " << flips << endl;
                ans ++;
                flips ++;
                down[i+k] = 1;
            }
        }
        for ( ; i < s.length(); i++)
        {
            flips -= down[i];
   //         cout << down[i] <<" " <<flips << endl;
            if ((s[i] == '-') ^ (flips & 1)) {
                no =1;
                break;
            }
        }

        printf( "Case #%d: ", ++cas);
        if ( no )
            printf( "IMPOSSIBLE\n" );
        else
            printf( "%d\n", ans );
	}
}
