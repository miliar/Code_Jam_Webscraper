#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define buybuy {printf("-1\n");return 0;}

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
//template<typename T> outln(T x) {cout << x; cout << "\n";}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n;"
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		
		int n = next();
		int c = next();
		int m = next();

		vector<vector<int>> pos(c);
		for (int i = 0; i < m; i++) {
			int p = next() - 1;
			int b = next() - 1;
			pos[b].pb(p);
		}

		vector<int> cnt(n, 0);
		for (auto p : pos) for (int pp : p) cnt[pp]++;

		int k = 0;
		for (auto p : pos) k = max(k, (int)p.size());

		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += cnt[i];
			k = max(k, (sum + i) / (i + 1));
		}
		
		int answ = 0;
		sum = 0;
		for (int i = 0; i < n; i++) {
			if (cnt[i] > k) answ += cnt[i] - k;
		}

		printf("Case #%d: %d %d\n", test, k, answ);
	}
}