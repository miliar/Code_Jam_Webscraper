#include <iostream>
#include <string>

using namespace std;

int happy(string &s, int k) {
	int ans = 0;
	int n = s.size();
	for (int i = 0, ie = n - k; i < ie; ++i) {
		if (s[i] == '+')
			continue;

		++ans;
		for (int j = i, je = i + k; j < je; ++j)
			s[j] = (s[j] == '+')? '-': '+';
	}

	char last = s.back();
	if (last == '-')
		++ans;
	for (int i = n - k; i < n; ++i)
		if (s[i] != last)
			return -1;
	return ans;
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << t << ": ";
		int ans = happy(s, k);
		if (ans >= 0)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
