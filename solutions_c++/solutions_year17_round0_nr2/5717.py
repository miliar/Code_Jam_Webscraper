#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		string s;
		cin>>s;

		int n = s.size(), pos = n;

		for(int i = n - 2; i >= 0; --i) {
			if(s[i] > s[i + 1]) {
				s[i] -= 1;
				pos = i + 1;
			}
		}
		if(s[0] == '0') {
			s.erase(s.begin());
			pos = 0;
		}

		for(int i = pos; i < n; ++i)
			s[i] = '9';

		cout << "Case #" << t << ": " << s << "\n";
	}

	return 0;
}
