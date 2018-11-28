#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool tidy(ll n) {
	stringstream ss;
	ss << n;

	string s = ss.str();

	for (int i = 1; i < s.size(); ++i)
		if (s[i-1] > s[i])
			return false;

	return true;
}

int main() {
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		ll n;
		cin >> n;

		while (not tidy(n)) n--;

		cout << "Case #" << t << ": " << n << endl;
	}


	return 0;

}
