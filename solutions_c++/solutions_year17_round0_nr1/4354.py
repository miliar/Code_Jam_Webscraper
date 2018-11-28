#include <bits/stdc++.h>
using namespace std;

int TC;

bool ok(vector<int> &v) {
	for(int z : v) {
		if(z % 2 != 0) return false;
	}
	return true;
}

int main() {
	cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		string s;
		int k;
		cin >> s >> k;
		int n = s.size();
		vector<int> v(n);
		for(int i = 0; i < n; ++i) {
			if(s[i] == '+') v[i] = 0;
			else v[i] = 1;
		}
		int ans = 0;
		for(int i = 0; i <= n - k; ++i) {
			if(ok(v)) break;
			if(v[i] % 2 != 0) {
				for(int j = i; j < i + k; ++j) v[j]++;
				++ans;
			}
		}
		cout << "Case #" << tc << ": ";
		if(ok(v)) cout << ans;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}