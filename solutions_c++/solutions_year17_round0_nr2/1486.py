#include <iostream>
#include <algorithm>

using namespace std;

typedef long long dint;

const int maxn = 45;

int n, a[maxn], b[maxn];

int DFS(int p, int d, int l) {
	if (p == n) {
		return 1;
	}
	if (d) {
		b[p] = a[p];
		if (b[p] >= l && DFS(p + 1, d, b[p])) {
			return 1;
		}
		for (b[p] = a[p] - 1; b[p] >= l; -- b[p]) {
			if (DFS(p + 1, 0, b[p])) {
				return 1;
			}
		}
	} else {
		b[p] = 9;
		return DFS(p + 1, d, 9);
	}
	return 0;
}

string sovB() {
	string s, ans("");
	cin >> s;
	n = s.length();
	for (int i = 0; i < n; ++ i) {
		a[i] = s[i] - 48;
	}
	DFS(0, 1, 0);
	int sp;
	for (sp = 0; sp + 1 < n && !b[sp]; ++ sp);
	for (; sp < n; ++ sp) {
		ans += (b[sp] + 48);
	}
	return ans;
}	

int main() {
#ifdef LAEKOV_LOCAL
	freopen(".in", "r", stdin);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++ i) {
		cout << "Case #" << i << ": " << sovB() << endl;
	}
}
