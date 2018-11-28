#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.length(); ++i)
			if (s[i] == '-') {
				++ans;
				if (i + k > s.length())
					break;
				for (int j = 0; j < k; ++j)
					if (s[i + j] == '+')
						s[i + j] = '-';
					else
						s[i + j] = '+';
			}
		for (int i = 0; i < s.length(); ++i)
			if (s[i] == '-')
				ans = -1;
		cout << "Case #" << t << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
	}
}