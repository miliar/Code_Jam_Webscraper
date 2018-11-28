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

inline bool tidy(i64 x) {
	int prev = 10;
	while(x) {
		int cur = x % 10;
		if (cur > prev)
			return 0;
		prev = cur;
		x /= 10;
	} 
	return 1;
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
		i64 n;
		cin >> n;
		vector<int> dig;
		while(n) {
			dig.pb(n % 10);
			n /= 10;
		}
		while(1) {
			//for(int x : dig) cerr << x;
			//cerr << endl;
			bool any = 0;
			for(int i = 1; i < (int)dig.size(); ++i) {
				if (dig[i] > dig[i-1]) {
					any = 1;
					--dig[i];
					for(int j = 0; j < i; ++j) {
						dig[j] = 9;
					}
					break;
				}			
			}
			if (!any) break;
		}
		bool begin = 1;
		cout << "Case #" << (test + 1) << ": ";
		reverse(dig.begin(), dig.end());
		for(int x : dig) {
			if (x == 0 && !begin) {
				cout << x;
				continue;
			}
			if (x == 0 && begin) {
				continue;
			}
			cout << x;
			begin = 0;
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