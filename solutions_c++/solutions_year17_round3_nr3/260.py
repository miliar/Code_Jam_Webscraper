#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("C-small-1-attempt1.in", "rt", stdin);
	freopen("C-small-1-attempt1.out", "wt", stdout);
	//freopen("test.in", "rt", stdin);
	//freopen("test.out", "wt", stdout);
#endif
}

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os<<"[";for(int i=0;i<v.size();i++)os<<" "<<v[i];os<<" ]";
    return os;
}

void solve() {
	int n, k; scanf("%d %d ", &n, &k);
	double u; scanf("%lf", &u);

	vector<double> v(n);
	REP(i, n) scanf("%lf ", &v[i]);

	sort(v.begin(), v.end());
	REP(i, n) {
		int cn = i + 1;
		double cap = (i == n - 1 ? 1.0 : v[i + 1]);
		double delta = cap - v[i];		
		if (delta * cn > u) delta = u / cn;
		REP(j, i + 1) {
			v[j] += delta;
			u -= delta;
		}
	}

	double prod = 1.0;
	REP(i, n) prod *= v[i];
	printf("%.10lf\n", prod);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
