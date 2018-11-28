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


const double eps = 10e-7;

void init() {

}

void clear(int i) {

}

int solution(int nTest) {
	double d;
	int n;
	scanf("%lf%d", &d, &n);
	vector<pair<double, double> > v;
	vector<double> tm;
	double res = 0.;
	cerr << nTest << endl;
	For (i, 0, n) {
		double k, s;
		scanf("%lf%lf", &k, &s);
		v.pb(mp(k, s));
		double t = (d - k) / s;
		res = max(res, t);
	}
	cerr << "AF" << endl;
	//sort(all(k, s));
	double l = 0;
	double r = 10e+10;
	/*
	while (r - l > eps) {
		double m = (r + l) / 2.;
		For (i, 0, sz(tm)) {
		}
	}
	*/
	double ans = d / res;
	printf("%.8lf\n", ans);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		cerr << i << endl;
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
