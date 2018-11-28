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
int e[111];
int s[111];
int d[111][111];
double dp[111][111];
i64 pd[111];

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
	for(int test = 1; test <= T; ++test) {
		int n, q;
		cin >> n >> q;
		for(int i = 0; i < n; ++i) {
			cin >> e[i] >> s[i];
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				cin >> d[i][j];
			}
		}
		double ans;
		int u, v;
		cin >> u >> v;
		pd[0] = 0;
		for(int i = 0; i < n; ++i) {
			pd[i+1] = pd[i] + d[i][i+1];
			for(int j = 0; j < n; ++j) {
				dp[i][j] = -1.0;
			}
		}
		dp[0][0] = 0.0;
		for(int i = 1; i < n; ++i) {
			for(int j = 0; j < i; ++j) {
				if (dp[i-1][j] < 0.0) continue;
				if (e[j] >= pd[i] - pd[j]) {
					dp[i][j] = dp[i-1][j] + double(d[i-1][i])/double(s[j]);
				}
			}
			for(int j = 0; j < i; ++j) {
				if (dp[i][j] >= 0.0 && (dp[i][i] < 0.0 || dp[i][i] > dp[i][j])) {
					dp[i][i] = dp[i][j];
				}	
			} 	
		}
		cout << fixed << setprecision(8);
		ans = -1.0;
		for(int i = 0; i < n; ++i) {
			if (dp[n-1][i] >= 0.0 && (ans < 0.0 || ans > dp[n-1][i])) {
				ans = dp[n-1][i];
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
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