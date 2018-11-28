#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
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
	//freopen("test.in", "rt", stdin);
	//freopen("test.out", "wt", stdout);
	// freopen("A-small-attempt0.in", "rt", stdin);
	// freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
}


map<vector<int>, int> states;
const int INF = 0x7FFFFFFF;

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os<<"[";for(int i=0;i<v.size();i++)os<<" "<<v[i];os<<" ]";
    return os;
}

int recur(const vector<int>& v, int p) {
	map<vector<int>, int>::iterator ii = states.find(v);
	if (ii != states.end()) {
		return ii->second;
	}
	int mod = v[0];
	int best = 0;

	bool hasNonZero = false;
	for (int i = 1; i < v.size(); i++) {
		if (v[i] > 0) {
			hasNonZero = true;
			int add = i - 1;
			vector<int> w = v;
			w[0] = (mod + add) % p;
			w[i]--;
			best = max(best, recur(w, p));
		}
	}
	if (!hasNonZero) return 0;

	best += (mod == 0 ? 1 : 0);
	states[v] = best;
	//cout << v << " -> " << states[v] << endl;

	return best;
}

void solve() {
	states.clear();
	int n, p; scanf("%d %d ", &n, &p);
	vector<int> v(p + 1);
	REP(i, n) {
		int a; scanf("%d ", &a);
		v[1 + (a % p)]++;
	}
	int ans = recur(v, p);
	printf("%d\n", ans);
}

void gen() {
	freopen("test.in", "wt", stdout);
	int T = 100;
	printf("%d\n", T);
	for (int t = 0; t < T; t++) {
		printf("%d %d\n", 100, 4);
		for (int i = 0; i < 100; i++) {
			printf("%d ", 1 + rand() % 100);
		}		
		printf("\n");
	}
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        cerr << i << endl;
        solve();
    }
    return 0;
}
