#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <set>
#include <assert.h>
#include <map>
#include <string.h>
using namespace std;

const int N = 1e6;
#define mp make_pair
typedef long long li;
typedef long double ld;

int k[N];
int v[N];
ld nk[N];
ld nv[N];


int n;
int d;
const ld EPS = 1e-9;

bool check(ld mid) {

	for (int i = 0; i < n; i++) {
		if ((ld)(mid - v[i]) < 0) continue;
		ld x = (ld)(k[i]) / (ld)(mid - v[i]);
		if (x < 0.0) continue;
		ld xp = (ld)k[i] + x * v[i];
		if (xp > (ld)d) continue;
		return false;
	}
	return true;
}

int main() {
#if _DEBUG
	freopen("A-large (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	
	int tests;
	cin >> tests;

	for (int test = 0; test < tests; test++) {
	
		cin >> d >> n;
		
		for (int i = 0; i < n; i++) {
			cin >> k[i] >> v[i];
		}

		ld l = 0.0, r = 5e15;

		for (int i = 0; i < 50000; i++) {
			ld mid = (l + r) / 2.0;
			if (check(mid))
				l = mid;
			else
				r = mid;
		}
		cout.precision(7);
		cout << "Case #" << test + 1 << ": " << fixed << l << endl;
	}

	return 0;
}