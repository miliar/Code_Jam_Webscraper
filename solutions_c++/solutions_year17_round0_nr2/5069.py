#include <cstdio>
#include <iostream>
typedef long long int ll;

using namespace std;

ll convert( string s ) {
    ll ret = 0;
    int h = 0;
    while ( s[h] == '0' ) {
	h++;
    }

    for ( int i = h; i < (int)s.length(); i++ ) {
	ret *= 10;
	ret += (s[i] - '0');
    }
    
    return ret;
}


int main()
{
    int T;
    scanf("%d", &T);

    for ( int t = 0; t < T; t++ ) {
	string N;
	cin >> N;

	for ( int i = 0; i < (int)N.length() - 1; i++ ) {
	    int a = N[i] - '0';
	    int b = N[i+1] - '0';
	    // 逆転
	    if ( a > b ) {
		int tail = i + 1;
		int cur = i;
		for ( int j = i + 1; j < (int)N.length(); j++ ) {
		    N[j] = '9';
		}
		N[cur] = ((10 + (N[cur] - '0') - 1) % 10) + '0';
		while ( cur > 0 ) {
		    int c = N[cur-1] - '0';
		    int d = N[cur] - '0';
		    if ( c <= d ) break;
		    else {
			N[cur] = '9';
			N[cur-1] = ((10 + (N[cur-1] - '0') - 1) % 10) + '0';
			cur--;
		    }
		}
		break;
	    }
	}
	ll ans = convert( N );
	printf("Case #%d: %lld\n", t+1, ans);
    }

    return 0;
}
