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

int main()
{
    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; ++t) {
	int n, k;
	cin >> n >> k;

	vector < int >parts;
	parts.push_back(n);

	for (int i = 1; i <= k; ++i) {
	    pop_heap(ALL(parts));
	    int e = parts.back();
	    parts.pop_back();

	    int x = e / 2;
	    int y = (e - 1) - x;

	    parts.push_back(x);
	    push_heap(ALL(parts));

	    parts.push_back(y);
	    push_heap(ALL(parts));

	    if (i == k) {
		cout << "Case #" << t << ": " << max(x, y) << " " << min(x,
									 y)
		    << "\n";
	    }

	}
    }
    return 0;
}
