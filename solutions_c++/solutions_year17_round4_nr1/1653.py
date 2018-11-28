#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}
#define PRINT(s, ...) {;}
#define PRINTLN(s, ...) {;}

// #undef HHHDEBUG
#ifdef HHHDEBUG
#include "template.h"
#endif

// for distributed code jam
// #include <message.h>
// #include ".h"

using namespace std;

template<typename T>
using Grid = vector<vector<T>>;

const double E = 1e-8;
const double PI = acos(-1);




int main() {
    ios::sync_with_stdio(false);

    int nt;
    cin >> nt;
    for (int it = 1; it <= nt; it++) {
    	int n, p; cin >> n >> p;
    	vector<int> m(p);
    	for (int i = 0; i < n; i++) {
    		int g;
    		cin >> g;
    		m[g % p]++;
    	}

    	int ans = m[0];
    	if (p == 2) {
    		ans += m[1] / 2;
    		if (m[1] % 2)
    			ans++;
    	}
    	else if (p == 3) {
    		int a = min(m[1], m[2]);
    		ans += a;
    		m[1] -= a;
    		m[2] -= a;
    		int left = max(m[1], m[2]);
    		ans += left / 3;
    		if (left % 3)
    			ans++;
    	}
    	else if (p == 4) {
    		int a = min(m[1], m[3]);
    		ans += a;
    		m[1] -= a;
    		m[3] -= a;
    		int b = max(m[1], m[3]);
    		ans += m[2] / 2;
    		if (m[2] % 2) {
    			if (b >= 2) {
    				ans++;
    				b -= 2;
    			}
    		}
			ans += b / 4;
			if (b % 4)
				ans++;
    	}
    	printf("Case #%d: %d\n", it, ans);
    }
}

