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


int a[3];
int first, last;
bool cmp(int i, int j) {
	if (i == last)
		return false;
	if (j == last)
		return true;
	if (a[i] != a[j])
		return a[i] > a[j];
	return i == first;
}
int getmxid() {
	vector <int> b = {0, 1, 2};
	sort(b.begin(), b.end(), cmp);
	return b[0];
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t; cin >> t;
	forn(i, t) {
		int n; cin >> n;
		int nul;
		forn(i, 3)
			cin >> a[i] >> nul;
		string c = "RYB";
		first = -1;
		last = -1;
		string res = "";
		forn(j, n) {
			int t = getmxid();
			if (!j)
				first = t;
			a[t]--;
			res += c[t];
			if (t == last || a[t] < 0) {
				res = "IMPOSSIBLE";
				break;
			}
			last = t;
			if (j + 1 == n && t == first)
				res = "IMPOSSIBLE";
		}
		cout << "Case #" << i + 1 << ": " << res << '\n';
	}
}