#include <string>
#include <iostream>
#include <cstring>

using namespace std;

char filp(char c) {
    if(c == '+') {
	return '-';
    }
    else {
	return '+';
    }
}

int main() {
    char s[1005];
    int k, t;
    cin >> t;
    for(int j = 1; j <= t; ++ j) {
	cin >> s >> k;
	int l = strlen(s);
	int ans = 0;
	for(int i = 0; i < l; ++ i) {
	    if(s[i] == '-') {
		if(i + k > l) {
		    ans = -1;
		    break;
		}
		else {
		    ans ++;
		    for(int ii = i+1; ii < i + k; ii ++) {
			s[ii] = filp(s[ii]);
		    }
		}
	    }
	}
	cout << "Case #" << j << ": ";
	if(ans >= 0) {
	    cout << ans << endl;
	}
	else {
	    cout << "IMPOSSIBLE" << endl;
	}
    }
    return 0;
}
