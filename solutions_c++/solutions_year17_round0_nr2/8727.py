#include <bits/stdc++.h>
using namespace std;
long long n;
vector<int> vi;
vector<int> v;
bool check(vector<int> vi) {
	int mx = vi[0];
	for (int i = 1; i < (int) vi.size(); i++) {
		mx = max(vi[i], mx);
		if (vi[i] < mx) {
			return 0;
		}
	}
	return 1;
}
int main() {
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	int cnt = 0;
	while (t--) {

		cin >> n;
		for (int i = 0; n; i++) {
			int x = n % 10;
			v.push_back(x);
			n /= 10;
		}
		reverse(v.begin(), v.end());
		while (!check(v)) {
			for (int j = v.size() - 1; j >= 0; j--) {
				for (int i = j - 1; i >= 0; i--) {
					if (v[i] > v[j]) {
						v[i]--;
						for (int k = i + 1; k < (int) v.size(); k++) {
							v[k] = 9;
						}
					}
				}
			}
		}

		int z = 0;
		for (int j = 0; j < (int) v.size(); j++) {
			if (v[j] == 0) {
				z = j + 1;
			} else {
				break;
			}
		}
		cout << "Case #" << ++cnt << ": ";
		for (int i = z; i < (int) v.size(); i++) {
			cout << v[i];
		}
		cout << endl;
		v.clear();

	}

}
