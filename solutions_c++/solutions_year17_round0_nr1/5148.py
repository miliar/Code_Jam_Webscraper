#include <iostream>
#include <cstdio>
#include <vector>

#define pb push_back

using namespace std;

int next() {int x; cin >> x; return x;}

int main() {

	int tests = next();
	string s;
	int k;
	for (int test = 1; test <= tests; test++) {
		cin >> s;
		cin >> k;
		//cout << "|" << s << "|" << "\n";

		vector<int> face;
		for (char c : s) face.pb(c == '-');

		int f = 0;
		int cnt = 0;
		vector<int> flip(s.size(), 0);

		for (int i = 0; i < s.size() - k + 1; i++) {
			if (face[i] != f) {
				flip[i] = 1;
				cnt++;
			}
			//cout << cnt << " " << f << " " << face[i] << "\n";
			f ^= flip[i];
			if (i >= k - 1) f ^= flip[i - k + 1];
		}
		bool ok = true;
		for (int i = s.size() - k + 1; i < s.size(); i++) {
			ok &= face[i] == f;
			if (i >= k - 1) f ^= flip[i - k + 1];
		}
		
		//for (int i = 0; i < s.size(); i++) cout << flip[i] << " ";
		//cout << "\n";

		if (ok) printf("Case #%d: %d\n", test, cnt);
		else printf("Case #%d: IMPOSSIBLE\n", test);
	}
}