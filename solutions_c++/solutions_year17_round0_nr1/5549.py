#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int flipper(string s, int k) {
	int c = 0;
	for(int i=0; i<s.length(); i++) {
		if(s[i] == '+') continue;
		if(i+k > s.length()) return -1;
		c++;
		for(int j=i; j<i+k; j++) {
			if(s[j] == '-') s[j] = '+';
			else s[j] = '-';
		}
	}
	return c;
}

int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }

		int t, k;
		string s;
    cin>>t;
    for(int i=1; i<t+1; i++) {
				cin >> s;
				cin >> k;
				printf("Case #%d: ", i);
				int res = flipper(s, k);
				if(res == -1) cout << "IMPOSSIBLE" << endl;
				else cout << res << endl;
    }
    return 0;
}
