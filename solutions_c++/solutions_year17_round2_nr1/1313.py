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

int T;
double k[1024];
double s[1024];

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
	cin >> T;
	cout << fixed << setprecision(8);
	for(int test = 1; test <= T; ++test) {
		int n;
		double d;
		cin >> d >> n;
		double l = 0.0;
		double r = 1e15;
		for(int i = 0; i < n; ++i) {
			cin >> k[i] >> s[i];
		}
		for(int it = 0; it < 256; ++it) {
			double m = 0.5*(l + r);
			bool any = 0;
			for(int i = 0; i < n; ++i) {
				if (s[i] >= m) continue;
				double t = k[i]/(m - s[i]);
				if (m*t <= d) {
					any = 1;
				}
			}
			if (any)
				r = m;
			else
				l = m;
		}
		cout << "Case #" << test << ": " << l << endl;
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