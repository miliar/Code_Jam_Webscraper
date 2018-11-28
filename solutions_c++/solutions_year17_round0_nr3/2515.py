#include <bits\stdc++.h>

using namespace std;

typedef long long ll;
#define N int(1e3+5)

int main() {
#define int ll
	ifstream cin("C-large.in");
	ofstream cout("output.txt");
	int t, n, k, ans;
	string s;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> n >> k;
		map<int, int> m;
		m.insert({ n, 1 });
		while (1) {
			auto it = *m.rbegin();
			if (k <= it.second) {
				ans = it.first;
				break;
			}
			k -= it.second;
			m.erase(it.first);
			if (it.first % 2)
				m[it.first / 2] += 2 * it.second;
			else {
				m[it.first / 2] += it.second;
				m[(it.first - 1) / 2] += it.second;
			}
		}
		cout << "Case #" << test << ": ";
		if (ans % 2)
			cout << ans / 2 << ' ' << ans / 2 << endl;
		else
			cout << ans / 2 << ' ' << (ans - 1) / 2 << endl;
	}
}