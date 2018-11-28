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

const double eps = 10e-7;
bool eq(double a, double b) {
	return fabs(a - b) < eps;
}
bool le(double a, double b) {
	return a < b || eq(a, b);
}


int solution(int nTest) {
	int n, p;
	scanf("%d%d", &n, &p);
	vector<int> r;
	For (i, 0, n) {
		int t;
		scanf("%d", &t);
		r.pb(t);
	}
	vector<pair<double, int> > v;
	For (i, 0, n) {
		For (j, 0, p) {
			int t;
			scanf("%d", &t);
			double s = ((double)t)/r[i];
			double rd = round(s);
			double val = fabs(rd - s)/rd;
			//cerr << t << "!" << s << " " << val << endl;
			if (le(val, 0.1)) {
				v.pb(mp(s, i));
			}
		}
	}
	vector<int> used(sz(v));
	sort(all(v));
	int res = 0;
	For (i, 0, sz(v)) {
		if (used[i]) {
			continue;
		}
		double m = v[i].first;
		map<int, int> ings;
		For (j, i, sz(v)) {
			if (used[j]) {
				continue;
			}
			double cur = v[j].first;
			int ing = v[j].second;
			if (ings.count(ing) != 0) {
				continue;
			}
			double mid = (cur + m) / 2;
			//cerr << m << " " << mid << " " << cur << endl;
			if (le((mid - m) / mid, .1)
					&& le((cur - mid) / mid, .1)) {

				ings[ing] = j;
				if (sz(ings) == n) {
					res++;
					for (map<int, int>::iterator it = ings.begin();
							it != ings.end(); it++) {

						used[it->second] = 1;
					}
					break;
				}
			}
		}
	}
	printf("%d\n", res);
			


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
	
