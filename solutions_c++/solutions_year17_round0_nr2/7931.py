#include <bits/stdc++.h>

#define sz(s) (int)s.size()
#define all(s) s.begin(),s.end()

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

string LongToString(ll a) {
	ostringstream temp;
	temp << a;
	return temp.str();
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {

		cout << "Case #" << i << ": ";

		ll x;
		int y;
		cin >> x;
		if (x < 10 && x > -1) {
			cout << x << endl;
			continue;
		}
		string s;
		s = LongToString(x);
		vector<int> v;
		for (int j = sz(s) - 1; j > 0; j--) {
			if (s[j] < s[j - 1]) {
				v.clear();
				y = s[j - 1] - '0';
				y--;
				s[j - 1] = y + '0';
				for (int k = j; k < sz(s); k++) {
					v.push_back(9);
				}
			} else {

				int z = s[j] - '0';
				v.push_back(z);
			}
		}

		if (s[0] != '0') {
			int z = s[0] - '0';
			v.push_back(z);
		}

		for (int i = sz(v) - 1; i >= 0; i--)
			cout << v[i];

		cout << endl;

	}

	return 0;
}
