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
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
}

const double EPS = 1e-7;

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os<<"[";for(int i=0;i<v.size();i++)os<<" "<<v[i];os<<" ]";
    return os;
}

template <class T>
ostream& operator<<(ostream& os, const vector<vector<T> >& v) {
	for (int i = 0; i < v.size(); i++) cout << v[i] << endl;
    return os;
}

int findMinK(int p, double r) {
	double ratio = p / r;
	double x = ratio / 1.1;
	int x1 = (x + EPS);

	for (int k = max(1, x1 - 5); k < x1 + 5; k++)
		if (1.1 * k * r + EPS > p && 0.9 * k * r - EPS < p)
			return k;

	return 0;
}

int findMaxK(int p, double r) {
	double ratio = p / r;
	double x = ratio / 0.9;
	int x1 = (x + EPS);

	for (int k = x1 + 5; k >= max(1, x1 - 5); k--)
		if (1.1 * k * r + EPS > p && 0.9 * k * r - EPS < p)
			return k;

	return 0;
}

void solve() {
	int n, m; scanf("%d %d ", &n, &m);
	vector<int> r(n);
	REP(i, n) scanf("%d ", &r[i]);

	vector<vector<int> > p(n, vector<int>(m));
	REP(i, n) REP(j, m) scanf("%d ", &p[i][j]);
	REP(i, n) sort(p[i].begin(), p[i].end());

	vector<int> idx(n, 0);

	bool over = false;
	int ans = 0;
	while (!over) {
		int minIngIdx = -1;		
		double minRatio = 1000000000.0;
		REP(i, n) {
			if (idx[i] == m) {
				over = true;
				break;
			}
			double ratio = findMinK(p[i][idx[i]], r[i]);
			if (ratio < minRatio) {
				minRatio = ratio;
				minIngIdx = i;
			}
		}

		if (!over) {			
			int maxK = findMaxK(p[minIngIdx][idx[minIngIdx]], r[minIngIdx]);
			//cout << minIngIdx << " -> " << maxK << endl;
			if (!maxK) {
				idx[minIngIdx]++;
				continue;
			}

			bool found = true;
			REP(i, n) {
				int minK = findMinK(p[i][idx[i]], r[i]);
				//cout << ":: " << i << " " << minK << endl;
				if (minK > maxK) {
					found = false;
				}
			}

			if (found) {
				ans++;
				REP(i, n) idx[i]++;
			} else {
				idx[minIngIdx]++;
			}
		}
	}

	printf("%d\n", ans);
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
