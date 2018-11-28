#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
#ifdef _DEBUG
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		ll n;
		cin >> n;

		vector<int> v;
		while (n > 0) {
			v.push_back(n % 10);
			n /= 10;
		}
		v.push_back(0);
		reverse(v.begin(), v.end());

		int k = 0;
		int tidy = true;
		for (; k + 1 < v.size() && tidy; k++) {
			tidy = (v[k] <= v[k + 1]);
		}

		if (!tidy) {
			k--;
			for (; k > 0 && !tidy; k--) {
				v[k]--;
				tidy = (v[k - 1] <= v[k]);
			}
			for (int i = k + 2; i < v.size(); i++) {
				v[i] = 9;
			}
		}

		for (k = 0; v[k] == 0; k++) {}
		for (; k < v.size(); k++) {
			cout << v[k];
		}
		cout << endl;
	}
	return 0;
}