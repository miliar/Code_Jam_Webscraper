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
		long double d; 
		int n; 
		cin >> d >> n;
		long double res = -1;
		forn(j, n) {
			long double k, s; cin >> k >> s;
			if (res == -1 || d / ((d - k) / s) < res)
			res = d / ((d - k) / s);
		}
		cout << "Case #" << i + 1 << ": " << setprecision(8) << fixed << res << '\n';
	}
}