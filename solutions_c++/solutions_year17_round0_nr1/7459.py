#include <iostream>
using namespace std;

void flip(string &s, int startIndex, int endIndex) {
	for (int i=startIndex; i<=endIndex; i++) {
		s[i] = (s[i] == '+') ? '-' : '+';
	}
}

int check(string s, int len, int k) {
	int ans = 0;
	int i = 0;
	for (; (i<len) && (i+k-1 < len); i++) {
		if (s[i] == '-') {
			flip(s, i, i+k-1);
			ans++;
		}
	}
	for (int i=0; i<len; i++) {
		if (s[i] == '-')
			return -1;
	}
	return ans;
}

int main() {
	int n, k, ans;
	string s;
	cin >> n;
	for (int t=0; t<n; t++) {
		cin >> s;
		cin >> k;
		int len = s.size();
		ans = check(s, len, k);
		cout << "Case #" << t+1 << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}