#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b)        __typeof(b) a=(b)
#define REP(i,n)        for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b)      for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b)     for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c)   for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c)          (c).begin(),(c).end()
#define TRACE(x)        cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x)        cerr << #x << " = " << x << endl;
#define eprintf(...)    fprintf(stderr, __VA_ARGS__)

typedef long long               ll;
typedef long double             ld;
typedef unsigned long           ulong;
typedef unsigned long long      ull;
typedef vector<int>             VI;
typedef vector<char>            VC;

int main() {
    //freopen("input",  "r", stdin);
    //freopen("output", "w", stdout);
	int TN;
	cin >> TN;
	FOR(TI,1,TN) {
		string s;
		int k;
		cin >> s >> k;
		int cnt = 0;
		FOR(i,0,s.size()-k) {
			if (s[i] == '-') {
				cnt++;
				REP(j,k) {
					s[i+j] = (s[i+j] == '-'? '+' : '-');
				}
			}
		}
		bool failed = false;
		FOR(i,s.size()-k, s.size()-1)
			if (s[i] == '-')
				failed = true;
		if (failed)
			printf("Case #%d: IMPOSSIBLE\n", TI);
		else
			printf("Case #%d: %d\n", TI, cnt);			
	}
    return 0;
}
