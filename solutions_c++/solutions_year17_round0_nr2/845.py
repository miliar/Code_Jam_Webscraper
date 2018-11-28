#include <bits/stdc++.h>
#define pb push_back
typedef long long ll;
const int N = 1e5 + 10;

using namespace std;

int test, id;

ll fun(ll x) {
	string s;
	while (x) {
		s = char (x % 10 + '0') + s;
		x /= 10;
	}
	bool ok;
	do {
		ok = false;
		for (int i = 0; i < s.length() - 1; i++) {
			if (s[i] > s[i + 1]) {
				ok = true;
				s[i]--;
				for (int j = i + 1; j < s.length(); j++) s[j] = '9';
				break;
			}
		}
	} while (ok);
	ll ret = 0;
	for (int i = 0; i < s.length(); i++) 
		ret = ret * 10 + (s[i] - '0');
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin >> test;
	while (test--) {
		id++;
		ll x;
		cin >> x;
		cout << "Case #" << id << ": " << fun(x) << endl;
	}
	return 0;
}