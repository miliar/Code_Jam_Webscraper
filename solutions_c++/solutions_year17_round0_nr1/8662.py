#include <iostream>
#include <string>
using namespace std;
string solve(string &s, int l) {
	int len(s.length());
	int	ans(0);
	for (int n(0);n<len;++n) {
		if (s[n] == '-')
		{
			++ans;
			for (int i(0); i < l; ++i)
			{
				s[n + i] = (s[n + i] == '-') ? '+' : '-';
			}
		}
		if ((len - n) <= l)
		{
			for (int i(n); i < len; ++i)
			{
				if (s[i] == '-')
					return "IMPOSSIBLE";
			}
			break;
		}
	}
	return to_string(ans);
}

int main() {
	int T;
	cin >> T;
	for (int cas(1); cas <= T; ++cas) {
		string s;
		int l;
		cin >> s>> l;
		cout << "Case #" << cas << ": " << solve(s,l) << endl;
	}
	return 0;
}
