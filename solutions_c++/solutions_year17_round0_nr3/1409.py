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

inline void add(map<i64, i64, greater<i64>> &mp, i64 x, i64 c) {
	auto it = mp.find(x);
	if (it == mp.end()) {
		mp.emplace(x, c);
	} 
	it -> y += c;
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
	for(int test = 0; test < T; ++test) {
		i64 n, k;
		map<i64, i64, greater<i64>> mp;
		cin >> n >> k;
		i64 ans = 0;
		mp.emplace(n, 1ll);
		while(1) {
			auto p = *mp.begin();
			mp.erase(mp.begin());
			if (p.y >= k) {
				ans = p.x;
				break;
			}
			k -= p.y;
			if (p.x & 1) {
				add(mp, p.x/2, 2*p.y);
			} else {
				add(mp, p.x/2, p.y);
				add(mp, p.x/2-1, p.y);
			}
		}
		cout << "Case #" << (test + 1) << ": ";
		if (ans & 1) {
			cout << ans/2 << ' ' << ans/2;	
		} else {
			cout << ans/2 << ' ' << ans/2 - 1;
		}
		cout << endl;
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