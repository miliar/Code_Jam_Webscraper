#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>

#define PI 3.14159265358979323846 
#define PO << " " <<
#define P " "
#define ABS(x) (((x) > 0) ? (x) : (-(x)))
#define RND(x) ((int)( (x) + 0.5 ))
#define MAX(x, y) (( (x) > (y) ) ? (x) : (y))
#define MIN(x, y) (( (x) < (y) ) ? (x) : (y))
#define forn(i, ending) for (int i = 0; i < (ending); i++)
#define it(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define oo ((double)2e9)

using namespace std;

typedef long long int lint;
typedef unsigned long long int ulint;
typedef std::pair <int, int> pint;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <vvi> vvvi;

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t; cin >> t;
	forn(i, t) {
		int n, q; cin >> n >> q;
		vector <double> e(n), s(n), d(n), time(n, -1);
		time[0] = 0;
		forn(i, n)
			cin >> e[i] >> s[i];
		forn(i, n)
			forn(j, n) {
				int k;
				cin >> k;
				if (i + 1 == j)
					d[i] = k;
			}
		forn(i, q) {
			int v, u; cin >> v >> u;
		}
		forn(i, n) if (time[i] != -1) {
			double tnow = time[i];
			for (int j = i + 1; j < n; j++) {
				e[i] -= d[j - 1];
				if (e[i] < 0)
					break;
				tnow += d[j - 1] / s[i];
				if (time[j] == -1 || tnow < time[j])
					time[j] = tnow;
			}
		}
		cout << "Case #" << i + 1 << ": " << setprecision(8) << fixed << time[n-1] << '\n';
	}
}