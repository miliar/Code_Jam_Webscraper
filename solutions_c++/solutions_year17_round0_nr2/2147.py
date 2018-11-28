#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define INF 2000000000
#define pb push_back
#define fs first
#define sc second
#define mp make_pair

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
typedef vector < int > VI;
typedef vector < unsigned int > VUI;
typedef vector < string > VS;
typedef vector < pair < int, int > > VII;


int main (int argc, char** argv) {
    
    // freopen(argv[1], "rt", stdin);
    // freopen(".out", "wt", stdout);

    int T;
    string s;

    cin >> T;
    for (int t = 1; t <= T; ++t) {
    	cin >> s;
    	if (s.length() == 1) {
    		cout << "Case #" << t << ": " << s << endl;
    		continue;
    	}

    	int maxPos1 = 0;
    	int maxPos2 = -1;
    	int l = s.length();
    	
    	for (int i = l - 2; i >= 0; --i)
    		if (s[i] > s[i + 1])
    			maxPos2 = i;

    	if (maxPos2 == -1) {
    		cout << "Case #" << t << ": " << s << endl;
    		continue;
    	}

		maxPos1 = maxPos2;
		while(s[--maxPos1] == s[maxPos2]) ;
		++maxPos1;

    	--s[maxPos1];
    	for (int i = maxPos1 + 1; i < l; ++i)
    		s[i] = '9';

    	if (s[0] == '0')
    		s = s.substr(1, s.length() - 1);

    	cout << "Case #" << t << ": " << s << endl;

    }

    return 0;
}
