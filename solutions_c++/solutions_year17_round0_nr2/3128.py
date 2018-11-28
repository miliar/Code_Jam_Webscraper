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
	unsigned long long ten[20], one[20];
	ten[0] = one[0] = 1;
	for ( int i = 1 ; i <= 18; i ++ ) ten[i] = ten[i-1] * 10;
	for ( int i = 1 ; i <= 18; i ++ ) one[i] = one[i-1] * 10 + 1;
	int T, cas = 0;
	cin>>T;
	while ( T -- )
	{
	    unsigned long long x;
		cin >> x;
		unsigned long long ans = 0;
		for ( int  i = 18; i >= 0; i -- )
        {
            unsigned long long p = x / ten[i];
            if ( p > 0 )
            {
                if ( p * one[i] <= x) ans += ten[i] * p;
                else {
                    ans += ten[i] * (p-1);
                    x = one[i-1] * 9;
                }
            }
            x %= ten[i];
        }
        printf( "Case #%d: ", ++cas);
        cout << ans << endl;
	}
	return 0;
}
