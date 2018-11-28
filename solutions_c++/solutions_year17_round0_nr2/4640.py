// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug = true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < VI > VVI;
typedef pair < int, int >PII;
typedef pair < int, PII > PIII;

bool make_it_tidier(string & s)
{
    for (int i = 1; i < SZ(s); ++i) {
	if (s[i - 1] > s[i]) {
	    s[i - 1] -= 1;
	    for (int j = i; j < SZ(s); ++j) {
		s[j] = '9';
	    }
	    if (s[0] == '0') {
		s.erase(0, 1);
	    }
	    return true;
	}
    }
    return false;
}

int main()
{
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; ++t) {
	string s;
	cin >> s;

	while (make_it_tidier(s));

	cout << "Case #" << t << ": " << s << "\n";

    }
    return 0;
}
