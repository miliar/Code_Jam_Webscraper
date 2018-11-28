#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

const long double eps = 1e-10;

int solution(int nTest) {
	int n, k;
	scanf("%d%d", &n, &k);
	double u;
	scanf("%lf", &u);
	vector<double> p;
	For (i, 0, n) {
		double t;
		scanf("%lf", &t);
		p.pb(t);
	}
	sort(all(p));
	long double l = 0, r = 1. + eps;
	while (r - l > eps) {
		long double m = (l + r) / 2.;
		long double n = 0;
		For (i, 0, sz(p)) {
			double t = p[i];
			if (t < m) {
				n += m - t;
			}
		}
		if (n <= u) {
			l = m;
		} else {
			r = m;
		}
	}


	cerr << l << endl;

	long double res = 1.;
	For (i, 0, sz(p)) {
		double t = p[i];
		if (t < l) {
			res *= l;
		} else {
			res *= t;
		}
	}
	printf("%.8Lf\n", res);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
