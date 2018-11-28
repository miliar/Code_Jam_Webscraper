#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define _with_file
#define TASK ""
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

void quit(); 

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
#ifdef local
typedef double ld;
#else
typedef long double ld;
#endif
typedef pair <int, int> PII;
typedef pair <i64, i64> PII64;
typedef pair <ld, ld> PLL;

const ld PI = acos(-1);
const ld EPS = 1e-10;
double __t;

inline string solve(int a, int b, int c, char aa, char bb, char cc) {
	string ans;
	for(int i = 0; i < a; ++i) {
		ans += aa;
		if (b > c) {
			--b;
			ans += bb;
			continue;
		}
		ans += cc;
		--c;
	} 
	while(b + c > 0) {
		if (ans.back() == bb) {
			ans += cc;
			--c;
		} else {
			ans += bb;
			--b;
		}
	}
	return ans;
}

int main()
{
	#ifdef local
		__t = clock();
		#ifndef _with_files
			freopen("z.in", "rt", stdin);
			freopen("z.out", "wt", stdout);
		#endif
	#endif
	#ifdef _with_files
		freopen(TASK".in", "rt", stdin);
		freopen(TASK".out", "wt", stdout);
	#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test) {
		int n;
		int r, o, y, g, b, v;
		cin >> n;
		cin >> r >> o >> y;
		cin >> g >> b >> v;
		//ryb
		int c = 0;
		set<int> cols;
		string col;
		if (r > 0) { 
			++c;
			col += "R";
			cols.insert(r);
		}
		if (y > 0)  {
			col += "Y";
		    cols.insert(y);
			++c;
		}
		if (b > 0) { 
			col += "B";
			cols.insert(b);
			++c;
		}	
		if (c == 1) {
			cout << "Case #" << test << ": IMPOSSIBLE" << endl;
			continue;
		}
		if (c == 2) {
			if (cols.size() != 1u) {
				cout << "Case #" << test << ": IMPOSSIBLE" << endl;
				continue;
			}
			cout << "Case #" << test << ": ";
			for(int i = 0; i < n; ++i) {
				cout << col[i%2];				
			}
			cout << endl;
			continue;
		}
		if (c == 3) {
			if (max({r, b, y}) > n - max({r, b, y})) {
				cout << "Case #" << test << ": IMPOSSIBLE" << endl;
				continue;
			}
			
			if (max({r, b, y}) == r) {
				cout << "Case #" << test << ": " << solve(r, b, y, 'R', 'B', 'Y') << endl;
				continue;
			}
			
			if (max({r, b, y}) == b) {
				cout << "Case #" << test << ": " << solve(b, r, y, 'B', 'R', 'Y') << endl;
				continue;
			}

			if (max({r, b, y}) == y) {
				cout << "Case #" << test << ": " << solve(y, r, b, 'Y', 'R', 'B') << endl;
				continue;
			}
		}
	}
	quit();
}

void quit()
{
	#ifdef local
		cerr << "\nTOTAL TIME: "<< (clock() - __t)/1000.0 << " s\n";
	#endif
	exit(0);		
}