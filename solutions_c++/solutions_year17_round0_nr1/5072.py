#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;

    scanf("%d", &T);
    
    for ( int t = 0; t < T; t++ ) {
	string s;
	int K;
	cin >> s;
	scanf("%d", &K);
	int ans = 0;

	for ( int i = 0; i < s.length() - K + 1; i++ ) {
	    if ( s[i] == '-' ) {
		ans++;
		for ( int j = i; j < i + K; j++ ) {
		    s[j] = (s[j] == '+') ? '-' : '+';
		}
	    }
	}

	bool enable = true;
	for ( int i = 0; i < s.length(); i++ ) {
	    if ( s[i] == '-' ) {
		enable = false;
		break;
	    }
	}

	if ( enable ) printf("Case #%d: %d\n", t+1, ans);
	else printf("Case #%d: IMPOSSIBLE\n", t+1);
    }

    return 0;
}
